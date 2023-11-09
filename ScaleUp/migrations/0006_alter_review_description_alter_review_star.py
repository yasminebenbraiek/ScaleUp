# Generated by Django 4.1.7 on 2023-03-30 01:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScaleUp', '0005_remove_partner_review_remove_partner_stars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(default='write review here', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
