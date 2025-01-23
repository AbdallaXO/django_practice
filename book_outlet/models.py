from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(null=True, max_length=60)
    is_bestselling = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return f"{self.title} Written By Best Selling Author {self.author} Rating: {self.rating}"
    
    