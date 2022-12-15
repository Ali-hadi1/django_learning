from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=50)
    # review_text = models.CharField(max_length=200)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return f"{self.username} {self.review_text} {self.rating}"
    