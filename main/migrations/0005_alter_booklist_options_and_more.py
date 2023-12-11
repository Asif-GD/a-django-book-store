# Generated by Django 5.0 on 2023-12-11 16:25

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_book_isbn_booklist_book_isbn_13'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booklist',
            options={'ordering': ['id'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.RenameField(
            model_name='booklist',
            old_name='book_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='booklist',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='booklist',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug'),
        ),
    ]
