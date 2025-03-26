import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    is_fixed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.CharField(max_length=100)
    competence_month = models.DateField(help_text='Competence Sample (ie: 2025-03-01)')
    payment_date = models.DateField()
    has_invoice = models.BooleanField(default=False)
    invoice_downloaded = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.description} - R${self.value} em {self.payment_date}'