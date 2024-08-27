from django.db import models
from django.contrib.auth.models  import User
from django.contrib.auth.models import AbstractUser, BaseUserManager



class Expense(models.Model):
    categories = (
    ('GROCERIES', 'groceries'),
    ('LEISURE', 'leisure'),
    ('ELECTRONICS', 'electronics'),
    ('UTILITIES', 'utilities'),
    ('CLOTHING', 'clothing'),
    ('HEALTH', 'health'),
    ('OTHERS', 'others')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categotry = models.CharField(max_length=50, choices=categories)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.categotry


