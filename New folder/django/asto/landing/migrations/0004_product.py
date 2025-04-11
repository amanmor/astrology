# Generated by Django 5.1.6 on 2025-04-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_alter_article_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('gemstone', 'Gemstone'), ('rudraksh', 'Rudraksh')], max_length=20)),
            ],
        ),
    ]
