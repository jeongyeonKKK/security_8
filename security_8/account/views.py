from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)


# Create your views here.


# def user_login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated', 'successfully')
#                 else:
#                     return HttpResponse('Disabled account')

#             else:
#                 return HttpResponse('Invalid login')
#         else:
#             form = LoginForm()
#     return render(request, 'account/login.html', {
#         'form': form
#     })

# def user_logout(request):
#     django_logout(request)
#     return redirect('post:post_list')