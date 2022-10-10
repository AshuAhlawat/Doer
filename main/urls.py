from django.urls import path
from . import views
from django.shortcuts import redirect

landing = lambda request: redirect("/dash")

urlpatterns = [
    path("dash/",views.dash),
    path("",landing),
    path("grouping/<int:id>/", views.grouping),
    path("grouping/new/", views.new_grouping),
    path("entry/<int:id>/", views.entry),
    path("entry/new/", views.new_entry),
    # path("feed/",views.feed),
]