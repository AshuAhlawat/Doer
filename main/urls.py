from django.urls import path
from . import views
from django.shortcuts import redirect

landing = lambda request: redirect("/dash")

urlpatterns = [
    path("",landing),
    path("dash/",views.dash),

    path("grouping/<int:id>/", views.grouping),
    path("grouping/new/", views.new_grouping),
    path("grouping/edit/<int:id>/", views.edit_grouping),
    path("grouping/delete/<int:id>/", views.delete_grouping),

    path("entry/<int:id>/", views.entry), 
    path("entry/new/", views.new_entry),
    path("entry/delete/<int:id>/", views.delete_entry),
    path("entry/edit/<int:id>/", views.edit_entry),
    # path("feed/",views.feed),
]