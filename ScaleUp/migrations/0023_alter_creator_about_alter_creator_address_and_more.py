# Generated by Django 4.1.7 on 2023-04-23 23:40

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ScaleUp', '0022_creator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='field',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='creator',
            name='job',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
