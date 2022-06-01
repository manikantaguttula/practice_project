
from django.db import models
class money(models.Model):
     name=models.CharField(max_length=25)
     address=models.TextField()
     phone=models.BigIntegerField(null=True)
     eid=models.CharField(max_length=30)
    # gender=models.BooleanField(default=None)
     def __str__(self):
         return self.name


# Create your models here.
