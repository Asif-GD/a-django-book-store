# Generated by Django 5.0 on 2023-12-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_booklist_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='book_isbn',
            field=models.IntegerField(unique=True),
        ),
    ]
