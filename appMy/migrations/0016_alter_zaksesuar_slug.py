# Generated by Django 4.1.5 on 2023-04-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0015_zaksesuar_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaksesuar',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='Slug Title'),
        ),
    ]
