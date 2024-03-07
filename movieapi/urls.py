from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup_api'),
    path('login/', views.login, name='login_api'),
]