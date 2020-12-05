"""SchoolProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from SchoolProject.views import hello_world,index_page,home_view,jquery_getRequest
from SchoolProject.views import AboutUs
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_world),
    path('',index_page),
    path('home/',home_view),
    path('jQget/',jquery_getRequest),
    path('about/',AboutUs.as_view()),
    path("student/",include("StudentApp.urls")),
]
