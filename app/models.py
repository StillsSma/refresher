from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    rating = models.DecimalField(decimal_places=3, max_digits=5)

    def pages_but_its_divided_by_ten(self):
        return int(self.pages)/10
