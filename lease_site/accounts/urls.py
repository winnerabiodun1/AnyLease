from knox import views as knox_views
from django.urls import path,include
from .views import SignUpView, LogInView, ChangePasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login' ),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('passwordreset/', include('django_rest_passwordreset.urls', namespace='passwordreset')),

]