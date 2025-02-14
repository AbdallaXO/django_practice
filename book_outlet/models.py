from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    def full_address(self):
        return f"\n{self.street} \n{self.city} \n{self.zip_code}"

    def __str__(self):
        return self.full_address()

    """ To manipualte how the model is viewed basically name of model or something
    since we cant do that with variables only with meta data."""

    class Meta:
        verbose_name_plural = "Address"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField(Country, related_name="books")

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} Written By {self.author.first_name} Rating: {self.rating}"
