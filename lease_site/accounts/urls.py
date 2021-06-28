from django.contrib import admin
from django.urls import path
from .views import SignUpView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', index, name='home'),
]