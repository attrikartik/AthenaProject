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
