# # from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.http.response import HttpResponse
# from django.urls import reverse_lazy
# from django.views import generic

# # Create your views here.
# class SignUpView (generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

# def index (request):
#     return HttpResponse ('Welcome to AnyLease Equipment Service')


from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Customer
from . serializers import CustomerSerializer

# making a Post request
class SignUpView (generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Making a GEt request
class SignUpView (generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer