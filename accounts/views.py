from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

from django.contrib.auth.models import User
from .models import Profile

from . import forms

def profile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
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
            profile = request.user.profile


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

def search(request):
    query = request.GET.get("query")
    data = {}
    if query:
        
        users = User.objects.filter(username__contains=query)
        data["query"] = query
        data["length"] = len(users)

        paginator = Paginator(users, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data["users_page"] = page_obj

    return render(request, "accounts/search.html", data)

def followers(request):
    data = {}
    if request.user.is_authenticated:
        profile = request.user.profile

        if request.method == "POST":
            follower = Profile.objects.get(id=request.POST["profile_id"])
            profile.followers.remove(follower)
            follower.following.remove(profile)

        followers_list = profile.followers.all()
        paginator = Paginator(followers_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data["profile_page`"] = page_obj 

    return render(request, "accounts/followers.html" , data)

def following(request):
    data = {}
    if request.user.is_authenticated:
        profile = request.user.profile

        if request.method == "POST":
            followed = Profile.objects.get(id=request.POST["profile_id"])
            profile.following.remove(followed)
            followed.followers.remove(profile)

        following_list = profile.following.all()
        paginator = Paginator(following_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data["profile_page"] = page_obj

    return render(request, "accounts/following.html" , data)

def signup(request):
    data = {}
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            user_profile = Profile(user = user)
            user_profile.save()
            
            return redirect("/accounts/login")

    creation_form = UserCreationForm()
    data["creation_form"] = creation_form
    
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