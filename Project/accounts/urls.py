from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
app_name="accounts"

urlpatterns=[
path('register/',views.Registration,name="register"),
path('',auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login")
]
