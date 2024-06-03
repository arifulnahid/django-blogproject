from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.name} | {self.email}'
