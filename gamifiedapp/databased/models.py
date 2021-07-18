from django.db import models

class Player(models.Model):
    gender = {("F", "female"), ("M", "male")}
    email = models.EmailField()
    # name = models.CharField(maxLength=30)
    def __str__(self) :
        return self.name