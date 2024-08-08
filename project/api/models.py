from django.db import models

# Create your models here.
class MovieModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "MovieModel"
        verbose_name_plural = "MovieModel"

    def __str__(self):
        return self.title    

