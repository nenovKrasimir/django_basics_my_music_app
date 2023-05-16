from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profile_app.models import Profile


# Create your models here.

class Album(models.Model):
    CHOICES = (
        ("Pop Music", "Other"),
        ("Jazz Music", "R&B Music"),
        ("Rock Music", "Country Music"),
        ("Dance Music", "Hip Hop Music")
    )
    name = models.CharField(blank=False, unique=True, max_length=30)
    artist = models.CharField(blank=False, max_length=30)
    genre = models.CharField(blank=False, max_length=30, choices=CHOICES)
    description = models.TextField(blank=True)
    image = models.URLField(blank=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
