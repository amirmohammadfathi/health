from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class Athlete(AbstractBaseUser):
    name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    is_male = models.BooleanField(default=True, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class CompleteInfo(models.Model):
    user = models.OneToOneField(Athlete, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)


class BodySize(models.Model):
    user = models.OneToOneField(Athlete, on_delete=models.CASCADE)
    wight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    shoulder = models.FloatField(null=True, blank=True)
    chest = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    high_hip = models.FloatField(null=True, blank=True)
    hip = models.FloatField(null=True, blank=True)
    shin = models.FloatField(null=True, blank=True)


class Disease(models.Model):
    user = models.OneToOneField(Athlete, on_delete=models.CASCADE)
    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    heart_failure = models.BooleanField(default=False)
    kidney_disease = models.BooleanField(default=False)
    cor_pulmoanle = models.BooleanField(default=False)
    backache = models.BooleanField(default=False)
    knee_pain = models.BooleanField(default=False)
