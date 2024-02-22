
# from django.contrib import admin
from django.urls import path
from home import views
from blog.views import home

urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("register/",views.register,name="register"),
    path("blog/",home,name="register")
  
]