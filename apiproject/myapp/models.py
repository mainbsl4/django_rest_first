from django.db import models

# Create your models here.

class ContractModal(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
