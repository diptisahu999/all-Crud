from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=34)
    email=models.EmailField()
    mobile=models.CharField(max_length=34)
    password=models.CharField(max_length=34)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table="asds"
