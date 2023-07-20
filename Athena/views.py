from django.shortcuts import render, redirect
from django.urls import reverse
from django import views
from django.contrib.auth import get_user_model, authenticate, login, logout

from .forms import *
from .models import *
from django.http import JsonResponse


# def load_profile(context, request):
#     user = request.user
#     if user.is_authenticated:
#         try:
#             old_profile = UserProfiles.objects.get(user=user)
#             context['profile_img'] = old_profile.img
#         except UserProfiles.DoesNotExist:
#             print('No User profile_img present')
#         return context
#     return context
#

# Create your views here.
class Dash(views.View):

    def get(self, request):
        context = {'title': 'Dashboard'}
        # load_profile(context, request)
        return render(request, 'Athena/dash_page.html', context)


class Courses(views.View):

    def get(self, request):
        context = {'title': 'Courses'}
        # load_profile(context, request)

        # trending_courses = Course.objects.order_by('-course_rating')[:5]
        # context['t_courses'] = trending_courses
        # # print(trending_courses)
        # # [print(x.course_title, x.course_rating) for x in trending_courses]
        # my_courses = Course.objects.filter(author=request.user)
        # context['my_courses'] = my_courses
        #
        # enrolled_courses = Enrollment.objects.filter(user=request.user)
        # context['e_courses'] = enrolled_courses
        #
        # view_courses = Course.objects.order_by('-course_rating')[:9]
        # context['v_courses'] = view_courses

        return render(request, 'Athena/course_page.html', context)


class Login(views.View):

    def get(self, request):
        context = {'title': 'Login'}
        return render(request, 'Athena/login.html', context)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        print("Login :", email, password)
        User = get_user_model()
        try:
            user_e = User.objects.get(email__exact=email)
        except User.DoesNotExist as e:
            print('New user, redirect to signin page')
            return redirect('signup_page')
        else:
            print(user_e.username)
            user = authenticate(request, username=user_e.username, password=password)
            if user is not None:
                login(request, user)
                print('Opening dashboard for the user {}'.format(user_e.username))
                return redirect('dash_page')
            else:
                print('Login password combination incorrect')
                return redirect('login_page')


class CourseDetails(views.View):

    def get(self, request, course_id):
        context = {'title': 'Course Details'}
        load_profile(context, request)
        course = Course.objects.get(id=course_id)

        if course.author == request.user:
            return redirect(reverse('course_author_page', args=[course_id]))

        author_profile = UserProfiles.objects.get(user=course.author)
        context['course'] = course
        context['author_profile'] = author_profile.img

        # Current User course details
        try:
            e_obj = Enrollment.objects.get(user=request.user, course=course)
        except Enrollment.DoesNotExist:
            e_obj = None
        context['e_obj'] = e_obj

        # All enrollment details
        enrollment_info = Enrollment.objects.filter(course=course)
        context['e_info'] = enrollment_info

        e_data = {
            'user': request.user,
            'course': course
        }
        e_form = EnrollmentForm(initial=e_data)

        e_form.fields['user'].widget.attrs['style'] = 'display: none;'
        e_form.fields['course'].widget.attrs['style'] = 'display: none;'

        context['e_form'] = e_form

        return render(request, 'Athena/course_details_page.html', context)


class EnrollCourse(views.View):

    def post(self, request):
        context = {}
        e_form = EnrollmentForm(request.POST)
        if e_form.is_valid():
            e_form.save()
            return redirect(reverse('course_details_page', args=[e_form.cleaned_data['course'].id]))
        else:
            return redirect('course_page')


def load_profile(context, request):
    user = request.user
    if user.is_authenticated:
        try:
            old_profile = UserProfiles.objects.get(user=user)
            context['profile_img'] = old_profile.img
        except UserProfiles.DoesNotExist:
            print('No User profile_img present')
        return context
    return context
