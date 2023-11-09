from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

from ScaleUp.decorators import allowed_users

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    about = models.TextField(null=True)
    field = models.CharField(max_length=200, null=True)
    country = CountryField(blank_label="(Select country)", null=True)
    date = models.DateField(null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    yt = models.URLField(null=True)
    yt_f = models.IntegerField(null=True)
    fb = models.URLField(null=True)  
    fb_f = models.IntegerField(null=True)  
    insta = models.URLField(null=True)
    insta_f = models.IntegerField(null=True)
    tt = models.URLField(null=True)
    tt_f = models.IntegerField(null=True)
    li = models.URLField(null=True)
    li_f = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    ref = models.CharField(unique=True, editable=True, max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    product_url = models.URLField(null=True) 
    image = models.ImageField(upload_to='scaleup/', null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# class Creator(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     image = models.ImageField(null=True)
#     about = models.TextField(null=True)
#     field = models.CharField(max_length=200, null=True)
#     job = models.CharField(max_length=200, null=True)
#     country = CountryField(blank_label="(Select country)", null=True)
#     birthday = models.DateField(null=True)
#     address = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.EmailField(null=True)
#     yt = models.URLField(null=True)
#     yt_f = models.IntegerField(null=True)
#     fb = models.URLField(null=True)  
#     fb_f = models.IntegerField(null=True)  
#     insta = models.URLField(null=True)
#     insta_f = models.IntegerField(null=True)
#     tt = models.URLField(null=True)
#     tt_f = models.IntegerField(null=True)
#     li = models.URLField(null=True)
#     li_f = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

class Partner(models.Model):
    STATUS_CHOICES = [
        ('Pending','P'),
        ('Approved','A'),
        ('Rejected','R'),
    ]
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

class Review(models.Model):
    SUBMIT_CHOICES = [
        ('Not submitted', 'No'),
        ('Submitted', 'Yes'),
    ]
    partner = models.OneToOneField(Partner, on_delete=models.SET_NULL, null=True)
    star= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],null=True, default=0)
    description = models.TextField(null=True, default="write review here")
    submit = models.CharField(max_length=20, choices=SUBMIT_CHOICES, default='Not submitted')

class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)