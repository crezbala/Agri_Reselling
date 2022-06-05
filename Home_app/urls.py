from django.urls import path
from . import views


urlpatterns = [
    path('', views.LandingPage,name="landingPage"),
    path('login/', views.LoginPage,name="login"),
    path('register/',views.reqregister,name="reqregister"),
    path('aboutReq/',views.aboutReq,name="aboutReq"),
    path('blogListReq/',views.blogReq,name="blogReq"),
    path('productReq/',views.productReq,name="productReq"),
    path('contactReq/',views.contactReq,name="contactReq"),
    path('testimonialReq/',views.testimonialReq,name="testimonialReq"),

]
