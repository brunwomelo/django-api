from django.db import models


# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=120)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']

    

