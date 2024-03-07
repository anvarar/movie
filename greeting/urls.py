"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from greeting import views as v2
urlpatterns = [ 
    path('Home/', v2.home,name='home'),
    path('addshow/', v2.addshow1,name='addshow1'),
    # path('list/', v2.list,name='list'),
    path('update/<int:id>/',v2.product_update,name='updateproduct'),
    path('delete/<int:id>',v2.product_delete,name='deleteproduct'),
    path('ten/<str:start_time>/',v2.ten,name='ten'),
    path('signup/',v2.signup,name='signup'),   
    path('',v2.login,name='login'),
]