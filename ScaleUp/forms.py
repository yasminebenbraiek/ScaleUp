from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Partner, Product, Post, Review 
from django.contrib.auth.models import User, Group

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'ref','user','name','category','release_date','price','product_url','image','about'}
        widgets = {
            'ref':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'release_date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'product_url':forms.URLInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class': 'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'product','user','name','description','image'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'product':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'user','name','about','image','field','country','date','address','phone','email','yt','yt_f','fb','fb_f','insta','insta_f','tt','tt_f','li','li_f'}
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control', 'rows': 4}),
            'image':forms.FileInput(attrs={'class': 'form-control'}),
            'field':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.Select(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'yt':forms.URLInput(attrs={'class':'form-control'}),
            'yt_f':forms.NumberInput(attrs={'class':'form-control'}),
            'fb':forms.URLInput(attrs={'class':'form-control'}),
            'fb_f':forms.NumberInput(attrs={'class':'form-control'}),
            'insta':forms.URLInput(attrs={'class':'form-control'}),
            'insta_f':forms.NumberInput(attrs={'class':'form-control'}),
            'tt':forms.URLInput(attrs={'class':'form-control'}),
            'tt_f':forms.NumberInput(attrs={'class':'form-control'}),
            'li':forms.URLInput(attrs={'class':'form-control'}),
            'li_f':forms.NumberInput(attrs={'class':'form-control'}),
        }

# class CreatorForm(forms.ModelForm):
#     class Meta:
#         model = Creator
#         fields = {'user','name','about','image','field','job','country','birthday','email','yt','yt_f','fb','fb_f','insta','insta_f','tt','tt_f','li','li_f'}
#         widgets = {
#             'user':forms.Select(attrs={'class':'form-control'}),
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'about':forms.Textarea(attrs={'class':'form-control', 'rows': 4}),
#             'image':forms.FileInput(attrs={'class': 'form-control'}),
#             'field':forms.TextInput(attrs={'class':'form-control'}),
#             'job':forms.TextInput(attrs={'class':'form-control'}),
#             'country':forms.Select(attrs={'class':'form-control'}),
#             'birthday':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
#             'address':forms.TextInput(attrs={'class':'form-control'}),
#             'phone':forms.NumberInput(attrs={'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'yt':forms.URLInput(attrs={'class':'form-control'}),
#             'yt_f':forms.NumberInput(attrs={'class':'form-control'}),
#             'fb':forms.URLInput(attrs={'class':'form-control'}),
#             'fb_f':forms.NumberInput(attrs={'class':'form-control'}),
#             'insta':forms.URLInput(attrs={'class':'form-control'}),
#             'insta_f':forms.NumberInput(attrs={'class':'form-control'}),
#             'tt':forms.URLInput(attrs={'class':'form-control'}),
#             'tt_f':forms.NumberInput(attrs={'class':'form-control'}),
#             'li':forms.URLInput(attrs={'class':'form-control'}),
#             'li_f':forms.NumberInput(attrs={'class':'form-control'}),
#         }

class CreateUserForm(UserCreationForm):

    group = forms.ModelChoiceField(queryset=Group.objects.all())
    
    class Meta:
        model = User
        fields = ['username','group','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'group':forms.Select(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        # def save(self, commit=True):
        #     user = super(CreateUserForm, self).save(commit=False)
        #     if commit:
        #         user.save()
        #     if user.group == 'Company':
        #         company = Company.objects.create(user=user)
        #         company.save()
        #     if user.group == 'Creator':
        #         creator = Creator.objects.create(user=user)
        #         creator.save()

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = {'product','user','status'}
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'product':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

class PartnerUpdateForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = {'status'}
        widgets = {
            'status':forms.Select(attrs={'class':'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'partner','star','description','submit'}
        widgets = {
            'partner':forms.Select(attrs={'class':'form-control'}),
            'star':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows': 4}),
            'submit':forms.Select(attrs={'class':'form-control'})

        }

