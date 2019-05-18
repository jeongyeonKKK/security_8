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
from hashlib import sha256
from random import getrandbits
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'account/index.html'
    
class CreateUSerView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

# SNARKs
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

def authentication(username, password):
    try:
        user = User.objects.get(username)

        lambda_key = getrandbits(256)

        witness = 'zk-snarks'.encode('utf-8') # secret parameter
        H = sha256(witness).hexdigest()

        pk, vk = G(lambda_key)

        false_witness = 'non-zk-snarks'.encode('utf-8')
        flase_proof = P(pk, H, false_witness)
        true_proof = P(pk, H, witness)
        verification = V(vk, H, true_proof)

        return verification

    except User.DoesNotExist:
        return False

# Login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.username
        password = form.password
        if authentication(username, password):
            return form
        else:
            return None

# Signup
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