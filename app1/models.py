from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.

POSITION_CHOICES = (
    ("1", "CEO"),
    ("2", "Director"),
    ("3", "Regional Manager"),
    ("4", "Entry Level"),
)



class Employees(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    password = models.CharField(max_length=100)
    options = models.CharField( max_length=20, choices=POSITION_CHOICES, default='4')
    work_under = models.ForeignKey( 'self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


    