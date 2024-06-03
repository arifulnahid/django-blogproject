from django.db import models
from author.models import Author

# Create your models here.


class Profile(models.Model):
    age = models.IntegerField()
    about = models.TextField()
    social = models.URLField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name
