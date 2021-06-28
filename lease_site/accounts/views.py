# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index (request):
    return HttpResponse ('Welcome to AnyLease Equipment Service')