from pyexpat import model
from unicodedata import name
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200)

class id_Brend_and_id_Category(models.Model):
    id_Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    id_Category = models.ForeignKey(Category, on_delete=models.CASCADE)