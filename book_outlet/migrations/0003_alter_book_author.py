# Generated by Django 5.1.4 on 2025-01-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Not Known', max_length=60),
            preserve_default=False,
        ),
    ]
