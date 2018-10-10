from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    course = models.IntegerField(default=1)
    department = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname
    


