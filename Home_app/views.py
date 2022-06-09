from django.shortcuts import render,redirect
from users.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser


def LandingPage(request):
    return render(request, "Home_app/index.html")

def LoginPage(request):
    #print(request.)
    print("login method print")

    #code change starts
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            task=CustomUser.objects.get(username=username)
            print("login method print 2")
            user1 = authenticate(request, username = username , password = password)
            if user1 is not None:
                print("success")
                login(request , user1)
                return redirect('landingPage')
            else:
                print("fail")
                context["err"]="Password is incorrect"
                context["username"]=username
        except:
            print("Something went wrong")
            context["err"]="Username does not exists"

    # code change ends
    return render(request, "Home_app/Login.html")

def reqregister(request):
    print("inside reqregister")
    #change starts
    context = {}
    if request.method == 'POST':  
        form= CustomUserCreationForm(request.POST)
        # print(request.POST.get('brandname'))
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request, user)
            print("a")
            return redirect('landingPage') 
        else:
            print("b")
            context['err']=form.errors.get_json_data()
            print(form.errors.get_json_data())
            context['username']=request.POST.get('username')
            context['email']=request.POST.get('email')  
    #change ends

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
