from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, SignupSerializer
# making a Post request

class SignUpView (generics.GenericAPIView):
    serializer_class = SignupSerializer
    
    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user" : UserSerializer(user, context=self.get_serializer_context()).data,
                "token" : AuthToken.objects.create(user)[1]
            })


from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LogInView (KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user) 
        return super(LogInView, self).post(request, format=None)
    

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import changePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = changePasswordSerializer
    
    model = User
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, queryset=None):
        query = self.request.user 
        return query
    
    def update(self,request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password" : ["wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status" : "Success",
                "code" : status.HTTP_200_OK,
                "message" : "Password Has Been Successfully Updated",
                "data" : []
            }
            
            return Response(response)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)