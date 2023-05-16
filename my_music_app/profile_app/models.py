from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=15, validators=(MinLengthValidator(2), RegexValidator(
            regex=r'^[a-zA-Z0-9_]+$',
            message="Ensure this value contains only letters, numbers, and underscore.",
            code='invalid_username')))

    email = models.EmailField(blank=False, null=True)
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])


