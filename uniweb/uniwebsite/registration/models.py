from django.db import models

# Create your models here.

class Student(models.Model):  
    name = models.CharField(max_length = 50)
    family = models.CharField(max_length = 100)
    mark = models.IntegerField()

    def __str__(self):
        return '{} - {}'  .format(self.name, self.family)