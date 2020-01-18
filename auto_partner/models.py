from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
from django.contrib import admin


class Partner(models.Model):
    id = models.IntegerField(blank=False, default=0, primary_key=True)
    name = models.CharField(blank=False, max_length=160)
    city = models.CharField(blank=False, max_length=200)
    address = models.CharField(blank=False, max_length=200)
    company_name = models.CharField(blank=False, max_length=200)
    assigned_autos = []
    created_at = UnixTimeStampField(auto_now_add=True)
    modify_at = UnixTimeStampField(auto_now=True)
    deleted_at = UnixTimeStampField(auto_now=True)
    autos = models.ManyToManyField('Auto', through='AutoPartnerRelation')

    def __str__(self):
        return str(self.id)


class Auto(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    average_fuel = models.IntegerField(default=0)
    delegation_starting = UnixTimeStampField(auto_now_add=True)
    delegation_ending = UnixTimeStampField(auto_now_add=True)
    driver = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    COMPANY = 'Company'
    PRIVATE = 'Private'
    type = models.CharField(
    choices=[(COMPANY, 'Company'), (PRIVATE, 'Private')], max_length=200)
    assigned_partners = []
    created_at = UnixTimeStampField(auto_now_add=True)
    modify_at = UnixTimeStampField(auto_now=True)
    deleted_at = UnixTimeStampField(auto_now=True)
    partners = models.ManyToManyField('Partner', through='AutoPartnerRelation')

    def __str__(self):
        return str(self.id)


class AutoPartnerRelation(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)


class AutoPartnerRelation_inline(admin.TabularInline):
    model = AutoPartnerRelation
    extra = 1


class partnerAdmin(admin.ModelAdmin):
    inlines = (AutoPartnerRelation_inline,)

class autoAdmin(admin.ModelAdmin):
    inlines = (AutoPartnerRelation_inline,)
