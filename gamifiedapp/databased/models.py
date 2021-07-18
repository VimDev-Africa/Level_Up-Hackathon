from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)
    gender = {("F", "female"), ("M", "male")}
    email = models.EmailField()
    age = models.IntegerField()
    
    # name = models.CharField(maxLength=30)
    def __str__(self) :
        return self.name
    
class Objective(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField()

