from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    gender_choices = (
        ("Male","Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )
    user = models.OneToOneField(User, models.CASCADE,related_name="profile")
    about = models.TextField(blank=True)
    
    dp = models.ImageField(default = "images/defaults/dp.png", upload_to = "images/dps/")
    phone = models.CharField(blank=True, max_length=13)
    gender = models.CharField(blank=True, choices=gender_choices, max_length=7)
    bday = models.DateField(blank=True,null=True)

    followers = models.ManyToManyField('self',blank=True,related_name='user_followers',symmetrical=False)
    following = models.ManyToManyField('self',blank=True,related_name='user_following',symmetrical=False)

    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"