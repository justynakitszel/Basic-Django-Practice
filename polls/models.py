from django.db import models

class Snippet(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=9)
    extra_info = models.TextField(max_length=200)

    def __str__(self):
        return self.name
