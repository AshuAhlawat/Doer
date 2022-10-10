from django.db import models

from django.contrib.auth.models import User


class Grouping(models.Model):
    title = models.CharField(max_length=60)
    done = models.BooleanField(default=False)

    user = models.ForeignKey(User, models.CASCADE, related_name="groupings")
    entries = models.ManyToManyField("Entry",blank=True,related_name="groupings")
    
    created = models.DateField(auto_created=True, auto_now_add=True)

    def __str__(self):
        if len(self.title)<=15:
            return f"{self.title}"
        else:
            return f"{self.title[:13]}..."
    
    def num_entries(self):
        return len(self.entries.all())

class Entry(models.Model):
    image = models.ImageField(upload_to="images/entries/", blank=True)
    title = models.CharField(max_length=60,blank=True)
    content = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    user = models.ForeignKey(User, models.CASCADE,related_name="entries")

    def __str__(self):
        if self.title:
            return self.title[:15]
        else:
            return "No Title" +self.content[:10]
