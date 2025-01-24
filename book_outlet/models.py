from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(null=True,max_length=60)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default=title, null=False)
    
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    """
    overwrides the save method and before we save, it makes for example abdalla akram abdalla-akram
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title} Written By {self.author} Rating: {self.rating}"
    
    