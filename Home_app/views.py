from django.shortcuts import render



def LandingPage(request):
    return render(request, "Home_app/index.html")

def LoginPage(request):
    #print(request.)
    print("login method print")
    return render(request, "Home_app/Login.html")

def reqregister(request):
    print("inside reqregister")
    return render(request, "Home_app/register.html")

def aboutReq(request):
    print("inside aboutreq")
    return render(request, "about.html")

def testimonialReq(request):
    print("inside testimonialReq")
    return render(request,"testimonial.html")

def blogReq(request):
    print("inside blogReq")
    return render(request,"blog_list.html")

def contactReq(request):
    print("inside contactReq")
    return render(request,"contact.html")

def productReq(request):
    print("inside productReq")
    return render(request,"product.html")
    
# Create your views here.
