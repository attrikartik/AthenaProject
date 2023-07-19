from django.shortcuts import render, redirect
from django.urls import reverse
from django import views
from django.contrib.auth import get_user_model, authenticate, login, logout
# from .forms import *
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
