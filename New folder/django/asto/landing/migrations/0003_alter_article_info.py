# Generated by Django 5.1.6 on 2025-04-01 04:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='info',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
