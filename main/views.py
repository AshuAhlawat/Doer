from django.shortcuts import render,redirect

from .models import Grouping, Entry
from .forms import GroupingForm, EntryForm


# -----------------------------BASICS-----------------------------

def dash(request):
    data = {}
    if request.user.is_authenticated:
        data["groupings"] = request.user.groupings.all()
        data["entries"] = request.user.entries.filter(groupings=None)

    return render(request, "main/dash.html", data)




# ---------------------------GROUPINGS----------------------------

def grouping(request,id):
    data = {}
    if request.user.is_authenticated:
        try:
            g = request.user.groupings.get(id = id)
        except:
            return redirect("/")

        if request.method == "POST":
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




# -------------------------------ENTRIES-------------------------------

def entry(request,id):
    data = {}
    if request.user.is_authenticated:
        entry = Entry.objects.get(id = id)
        if entry.user != request.user:
            return redirect("/")

        if request.method == "POST":
            pass
        
        gid = request.GET.get("grouping")
        if gid:
            grouping = request.user.groupings.get(id = gid)
            data["grouping"] = grouping
        data["entry"] = entry 
    else:
        return redirect("/accounts/login")

    return render(request, "main/entry.html", data)

def new_entry(request):
    data = {}
    if request.user.is_authenticated:
        gid = request.GET.get("grouping")
        if gid:
            gid = int(gid)

        if request.method == "POST":
            entry_form = EntryForm(request.POST.copy(),request.FILES)
            entry_form.data["user"] = request.user

            if entry_form.is_valid():
                entry = entry_form.save()
                added_to = request.POST.getlist('added_to')
                
                if added_to:
                    for i in added_to:
                        group = Grouping.objects.get(id=i)
                        group.entries.add(entry)
                    return redirect(f"/grouping/{gid}/")
                else:
                    return redirect("/")
        
        entry_form = EntryForm()
        entry_form.fields["title"].initial = "No Title"

        data["entry_form"] = entry_form
        data["groupingid"] = gid

    else:
        return redirect("/accounts/login")

    return render(request, "main/new_entry.html", data)

def delete_entry(request, id):
    data= {}
    if request.user.is_authenticated:
        entry = Entry.objects.get(id = id)
        if entry.user != request.user:
            return redirect("/")


        gid = request.GET.get("grouping")
        if gid:
            grouping = Grouping.objects.get(id=gid)
            data["grouping"] = grouping
        
        if request.method == "POST":
            process = request.POST["process"]

            if process == "perma":
                entry.delete()
                return redirect("/")
            elif process == "all":
                for grouping in entry.groupings.all():
                    grouping.entries.remove(entry)
                return redirect("/")
            else:
                grouping.entries.remove(entry)
                return redirect(f"/grouping/{grouping.id}/")
                
                # if gid:

        data["entry"] = entry
    else:
        return redirect("/")    
    
    return render(request, "main/delete_entry.html",data)