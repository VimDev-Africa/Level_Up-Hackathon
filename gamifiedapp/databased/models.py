from django.db import models

class Player(models.Model):
    kind = {("F", "female"), ("M", "male")}
    email = models.EmailField(unique=True)
    name = models.CharField()
    def __str__(self) :
        return self.name