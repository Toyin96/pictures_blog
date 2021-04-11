from django.db import models


# Create your models here.

class Picture(models.Model):
    """Defines a picture object"""
    image = models.FilePathField(path="/img")
    image_desc = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)
    contributor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.image}\n" \
               f"{self.image_desc}\n" \
               f"{self.added_date}\n" \
               f"{self.contributor}\n"
