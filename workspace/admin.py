from django.contrib import admin

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    model = models.Company
    list_display = ['code', 'name', 'email']


@admin.register(models.Operator)
class OperatorAdmin(admin.ModelAdmin):
    model = models.Operator
    list_display = ['code', 'name', 'email', 'turn']


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    model = models.Person
    list_display = ['name', 'mobile_number', 'email']


@admin.register(models.GroupProduct)
class PersonAdmin(admin.ModelAdmin):
    model = models.GroupProduct
    list_display = ['code', 'name']
