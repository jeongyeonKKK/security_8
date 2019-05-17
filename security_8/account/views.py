from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.contrib.auth.models import User

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


from hashlib import sha256
from random import getrandbits




from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = 'account/index.html'



def C(x, w):
    return sha256(w).hexdigest() == x

def G(l):
    pk = l + id(C)
    vk = l - id(C)

    return pk, vk

def P(pk, x, w):
    proof = pk + C(x, w)
    return proof

def V(vk, x, proof):
    correct_proof = vk + 2 * id(C) + 1
    return proof == correct_proof


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        lambda_key = getrandbits(256)

        witness = 'zk-snarks'.encode('utf-8')
        H = sha256(witness).hexdigest()

        pk, vk = G(lambda_key)

        false_witness = 'non-zk-snarks'.encode('utf-8')
        false_proof = P(pk, H, false_witness)
        false_verification = V(vk, H, false_proof)
        print(false_witness, false_proof, false_verification)

        proof = P(pk, H, witness)
        verification = V(vk, H, proof)
        print(witness, proof, verification)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.cleaned_data)
            login(request, new_user)
            return redirect('/account/login/')
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form':form})




class CreateUSerView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'