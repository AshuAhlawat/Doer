from django.shortcuts import render,redirect

from .models import Grouping, Entry
from .forms import GroupingForm, EntryForm


def dash(request):
    data = {}
    if request.user.is_authenticated:
        data["groupings"] = request.user.groupings.all()
        data["entries"] = request.user.entries.filter(groupings=None)

    return render(request, "main/dash.html", data)

def grouping(request,id):
    data = {}
    if request.user.is_authenticated:
        g = Grouping.objects.get(id = id)

        if request.method == "POST":
            g.title = request.POST["title"]
            for entry in g.entries.all():
                if request.POST.get(str(entry.id)):
                    entry.done = True
                else:
                    entry.done = False
                entry.save()
            g.save()


        data["grouping"] = g
        
        by = request.GET.get("by")
        reverse = request.GET.get("reverse")

        if not by:
            by = "created"
        
        data["by"] = by

        if reverse:
            by = "-" + by
            data["rev"] = "Reverse"
        
        data["entries"] = g.entries.order_by(by)      
    else:
        return redirect("/accounts/login")

    return render(request, "main/grouping.html", data)

def entry(request,id):
    data = {}
    if request.user.is_authenticated:
        data["entry"] = Entry.objects.get(id = id)
    else:
        return redirect("/accounts/login")

    return render(request, "main/entry.html", data)

def new_grouping(request):
    data = {}
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            grouping = Grouping(title=title, user=request.user)
            grouping.save()

            return redirect(f"/grouping/{grouping.id}/")

    else:
        return redirect("/accounts/login")

    return render(request, "main/new_grouping.html", data)

def new_entry(request):
    data = {}
    if request.user.is_authenticated:
        pass
    else:
        return redirect("/accounts/login")

    return render(request, "main/new_entry.html", data)