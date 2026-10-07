from tabnanny import verbose

from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students123"

    def __str__(self):
        return self.name


class Product():
    pass