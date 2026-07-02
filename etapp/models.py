from django.db import models

# Create your models here.

class Expense(models.Model):
    amount = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.amount
    

class Income(models.Model):
    amount = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.amount
   
