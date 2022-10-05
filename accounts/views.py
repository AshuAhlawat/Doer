from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

from django.contrib.auth.models import User
from .models import Profile

from . import forms

def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            dp = request.FILES.get('dp')
            if dp:
                profile.dp = dp
            profile_form = forms.ProfileForm(request.POST,instance=profile)
            request.user.first_name = request.POST["fname"]
            request.user.last_name = request.POST["lname"]
            
            profile_form.save()
            request.user.save()
        else:
            profile_form = forms.ProfileForm(instance=profile)
        
        # print(profile)
        
    else:
        return redirect("/accounts/login")  

    data = {
        'profile' : profile,
        "profile_form" : profile_form
    }

    return render(request, "accounts/profile.html", data)

def profile_other(request, username):
    followed = False
    try:
        user_other = User.objects.get(username=username)
        profile_other = Profile.objects.get(user = user_other)

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)


            if profile_other in profile.following.all():
                followed = True

            if request.method == "POST":
                if followed:
                    profile.following.remove(profile_other)
                    profile_other.followers.remove(profile)
                    followed = False
                else:
                    profile.following.add(profile_other)
                    profile_other.followers.add(profile)
                    followed = True

    except Exception as e:
        print(e)
        profile_other = None

    data = {
        "profile" : profile_other,
        "followed" : followed
    }
    
    return render(request, "accounts/profile_other.html", data)

def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            user_profile = Profile(user = user)
            user_profile.save()
            
            return redirect("/accounts/login")

    creation_form = UserCreationForm()

    data = {
        "creation_form" : creation_form
    }

    return render(request, "accounts/signup.html", data)

def login(request):
    error = ""
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],password=request.POST["password"])
        if user:
            auth.login(request, user)
            return redirect("/")
        else:
            error = "Wrong Username/Password"

    data = {
        "error":error
    }
    return render(request, "accounts/login.html",data)

def logout(request):
    if request.user.is_authenticated:
        msg = "See you later "+request.user.username
        auth.logout(request)
    else:
        msg = "Need to login first dummy"

    data = {
        "msg" : msg
    }

    return render(request, "accounts/logout.html", data)