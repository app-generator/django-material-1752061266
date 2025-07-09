# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    billing_address = models.TextField(max_length=255, null=True, blank=True)
    shipping_address = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Inventoryitem(models.Model):

    #__Inventoryitem_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    cost_price = models.IntegerField(null=True, blank=True)
    markup_percent = models.IntegerField(null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    stock_level = models.IntegerField(null=True, blank=True)
    reorder_level = models.IntegerField(null=True, blank=True)
    supplier = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()

    #__Inventoryitem_FIELDS__END

    class Meta:
        verbose_name        = _("Inventoryitem")
        verbose_name_plural = _("Inventoryitem")


class Inventoryadjustment(models.Model):

    #__Inventoryadjustment_FIELDS__
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Inventoryadjustment_FIELDS__END

    class Meta:
        verbose_name        = _("Inventoryadjustment")
        verbose_name_plural = _("Inventoryadjustment")


class Billofmaterials(models.Model):

    #__Billofmaterials_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    decsription = models.TextField(max_length=255, null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    markup_percent = models.IntegerField(null=True, blank=True)

    #__Billofmaterials_FIELDS__END

    class Meta:
        verbose_name        = _("Billofmaterials")
        verbose_name_plural = _("Billofmaterials")


class Bomitem(models.Model):

    #__Bomitem_FIELDS__
    bom = models.ForeignKey(BillOfMaterials, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.DateTimeField(blank=True, null=True, default=timezone.now)
    unit_cost = models.IntegerField(null=True, blank=True)

    #__Bomitem_FIELDS__END

    class Meta:
        verbose_name        = _("Bomitem")
        verbose_name_plural = _("Bomitem")


class Quote(models.Model):

    #__Quote_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quote_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)

    #__Quote_FIELDS__END

    class Meta:
        verbose_name        = _("Quote")
        verbose_name_plural = _("Quote")


class Quoteitem(models.Model):

    #__Quoteitem_FIELDS__
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True, blank=True)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    bom = models.ForeignKey(BillOfMaterials, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

    #__Quoteitem_FIELDS__END

    class Meta:
        verbose_name        = _("Quoteitem")
        verbose_name_plural = _("Quoteitem")


class Jobcard(models.Model):

    #__Jobcard_FIELDS__
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    job_number = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    assigned_to = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Jobcard_FIELDS__END

    class Meta:
        verbose_name        = _("Jobcard")
        verbose_name_plural = _("Jobcard")


class Jobcardfile(models.Model):

    #__Jobcardfile_FIELDS__
    jobcard = models.ForeignKey(JobCard, on_delete=models.CASCADE)
    file = models.CharField(max_length=255, null=True, blank=True)
    uploaded_by = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    file_type = models.CharField(max_length=255, null=True, blank=True)

    #__Jobcardfile_FIELDS__END

    class Meta:
        verbose_name        = _("Jobcardfile")
        verbose_name_plural = _("Jobcardfile")


class Jobcardactivity(models.Model):

    #__Jobcardactivity_FIELDS__
    jobcard = models.ForeignKey(JobCard, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    changed_by = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Jobcardactivity_FIELDS__END

    class Meta:
        verbose_name        = _("Jobcardactivity")
        verbose_name_plural = _("Jobcardactivity")


class Systemsettings(models.Model):

    #__Systemsettings_FIELDS__
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    quote_prefix = models.IntegerField(null=True, blank=True)
    job_prefix = models.IntegerField(null=True, blank=True)
    next_quote_number = models.IntegerField(null=True, blank=True)
    next_job_number = models.IntegerField(null=True, blank=True)
    default_markup_percent = models.IntegerField(null=True, blank=True)
    terms_and_conditions = models.TextField(max_length=255, null=True, blank=True)

    #__Systemsettings_FIELDS__END

    class Meta:
        verbose_name        = _("Systemsettings")
        verbose_name_plural = _("Systemsettings")


class Company(models.Model):

    #__Company_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")



#__MODELS__END
