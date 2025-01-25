# Generated by Django 5.1.4 on 2025-01-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0010_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='book_outlet.country'),
        ),
    ]
