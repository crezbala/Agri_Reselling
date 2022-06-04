from django.shortcuts import render



def LandingPage(request):
    return render(request, "Home_app/index.html")

def LoginPage(request):
    print("login method print")
    return render(request, "Home_app/Login.html")

def reqregister(request):
    print("inside reqregister")
    return render(request, "Home_app/register.html")

    
# Create your views here.
