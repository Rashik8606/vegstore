from django.db import models

# Create your models here.

class Email_sub(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class ownerdescription(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    typeofcultivation = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name




