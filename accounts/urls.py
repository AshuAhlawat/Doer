from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/',views.login),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('profile/<str:username>', views.profile_other),    
    path('following/',views.following),
    path('followers/',views.followers),
    path('search/',views.search),
]