from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import Choices

c = Choices()
GENDER_CHOICES = Choices().gender()

class Company(models.Model):
    code = models.IntegerField(unique=True, null=False, auto_created=True, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    email = models.EmailField(blank=True, verbose_name=_('email'))
    
    def __str__(self):
        return self.name


class Person(models.Model):
    document_number = models.IntegerField(unique=True, null=False, verbose_name=_('document number'))
    nickname = models.CharField(max_length=100, verbose_name=_('nickname'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name=_('gender'))
    code_area = models.CharField(max_length=2, null=True, verbose_name=_('code area'))
    mobile_number = models.CharField(max_length=10, verbose_name='mobile_number')
    email = models.EmailField(null=True, blank=True, verbose_name='email')

    def __str__(self):
        return self.name


class Operator(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    code = models.IntegerField(unique=True, null=False, auto_created=True, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    email = models.EmailField(blank=True, verbose_name=_('email'))
    turn = models.CharField(max_length=10, null=False, verbose_name=_('turn'))
    
    def __str__(self):
        return self.name


class GroupProduct(models.Model):
    code = models.IntegerField(unique=True, null=False, auto_created=True, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))

    def __str__(self):
        return self.name
