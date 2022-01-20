from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='register'),
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.LoginUser,name='login'),
    path('student/',views.student,name='student'),
]
