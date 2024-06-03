from django.db import models
from author.models import Author
from categories.models import Category

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    content = models.TextField()
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
