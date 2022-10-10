from django.forms import ModelForm
from . import models

class GroupingForm(ModelForm):
    class Meta:
        model = models.Grouping
        fields = ["title"]

class EntryForm(ModelForm):
    class Meta:
        model = models.Entry
        exclude = ["created","edited","user"]
        