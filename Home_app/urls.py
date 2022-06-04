from django.urls import path
from . import views


urlpatterns = [
    path('', views.LandingPage),
    path('login/', views.LoginPage,name="login"),
    path('register/',views.reqregister,name="reqregister"),


]
