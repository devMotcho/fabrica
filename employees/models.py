from django.db import models

class Operator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
