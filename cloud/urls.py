"""cloud URL Configuration

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
from . import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('user_login/',views.user_login, name = "user_login"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('add_post',views.add_post, name = "add_post"),
    path('read_post',views.read_post, name = "read_post"),





    # path('update_post',views.update_post, name = "update_post"),
    # path('delete_post',views.delete_post, name = "delete_post"),
    path('add_user',views.add_user, name = "add_user"),
    path('read_user',views.read_user, name = "read_user"),

]

