# Generated by Django 4.2.2 on 2023-06-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_url_times_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]