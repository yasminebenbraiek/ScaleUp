# Generated by Django 4.1.7 on 2023-04-26 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ScaleUp', '0025_remove_partner_creator_remove_product_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('about', models.TextField(null=True)),
                ('field', models.CharField(max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('date', models.DateField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('yt', models.URLField(null=True)),
                ('yt_f', models.IntegerField(null=True)),
                ('fb', models.URLField(null=True)),
                ('fb_f', models.IntegerField(null=True)),
                ('insta', models.URLField(null=True)),
                ('insta_f', models.IntegerField(null=True)),
                ('tt', models.URLField(null=True)),
                ('tt_f', models.IntegerField(null=True)),
                ('li', models.URLField(null=True)),
                ('li_f', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='creator',
            name='user',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Creator',
        ),
    ]