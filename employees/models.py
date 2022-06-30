from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    

