from django.urls import path
from . import views
from django.shortcuts import redirect

landing = lambda request: redirect("/dash")

urlpatterns = [
    path("dash/",views.dash),
    # path("feed/",views.feed),
    path("",landing)
]