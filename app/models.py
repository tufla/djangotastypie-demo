from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    created = models.DateField()


class Stock(models.Model):
    company = models.ForeignKey(Company)
    Date = models.DateField()
    Open = models.FloatField(null=True, blank=True)
    High = models.FloatField(null=True, blank=True)
    Low = models.FloatField(null=True, blank=True)
    Close = models.FloatField(null=True, blank=True)
    Volume = models.FloatField(null=True, blank=True)
    Adj_Close = models.FloatField(null=True, blank=True)
    Symbol = models.CharField(max_length=200)
