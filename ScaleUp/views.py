from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ScaleUp.decorators import allowed_users, unauthenticated_user
from django.db.models import Q
from ScaleUp.models import Category, Product, Post, Partner, Profile, Review
from .forms import PartnerForm, PartnerUpdateForm, ProductForm, PostForm, CreateUserForm, ProfileForm, ReviewForm
# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = form.cleaned_data['group']
            user.groups.add(group)
            profile = Profile.objects.create(user=user)
            login(request, user)
            return redirect('updateProfile')
        else:
            messages.error(request,'Error occured during registration')

    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Incorrect username or password')
    
    context={}
    return render(request, 'login.html', context) 

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def products(request):
    user = request.user
    groups = user.groups.filter(Q(name='Creator') | Q(name='Company'))
    group = str(groups[0].name)              
    products = Product.objects.filter(user=user)
    if group == 'Company': 
        products = Product.objects.filter(user=user)
    if group == 'Creator':        
        products = Partner.objects.filter(user=user)
    context = {'products' : products, 'group':group}
    return render(request,'products.html', context)

@login_required
def posts(request):
    user = request.user
    groups = user.groups.filter(Q(name='Creator') | Q(name='Company'))
    group = str(groups[0].name)
    posts = Post.objects.all()
    categories = Category.objects.all()
    if group == 'Company':            
            posts = Post.objects.filter(user=user)
    context = {'posts' : posts, 'categories':categories ,'group':group}
    return render(request,'posts.html', context)

@login_required
def partners(request):
    user = request.user
    groups = user.groups.filter(Q(name='Creator') | Q(name='Company'))
    group = str(groups[0].name)
    partners = Partner.objects.none
    products = Product.objects.filter(user=user)
    print(products)
    if group == 'Creator':
        partners = Partner.objects.filter(user=user)
        for p in partners:
            if p.product == None:
                p.delete()
    if group == 'Company':
        partners = Partner.objects.none()
        for p in products:
            partners |= Partner.objects.filter(product=p)
    print(partners)
    context = {'partners' : partners, 'group':group}
    return render(request,'partners.html', context)

@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request,'productForm.html', context)

@login_required
def updateProduct(request, pk):
    product = Product.objects.get(ref=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        
    context = {'form':form}
    return render(request, 'productForm.html', context)

@login_required
def deleteProduct(request, pk):
    product = Product.objects.get(ref=pk)
    product.delete()
    return redirect('products')

@login_required
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form':form}
    return render(request,'postForm.html', context)

@login_required
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
    context = {'form':form}
    return render(request, 'postForm.html', context)

@login_required
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('posts')

@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    groups = user.groups.filter(Q(name='Creator') | Q(name='Company'))
    group = str(groups[0].name)
    context = {'profile':profile, 'group':group}
    return render(request,'profile.html', context)

@login_required
def updateProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES ,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    context = {'form':form}
    return render(request, 'ProfileForm.html', context)

@login_required
def productTry(request,pk):
    user = request.user
    groups = user.groups.filter(Q(name='Creator') | Q(name='Company'))
    group = str(groups[0].name)
    product = Product.objects.get(ref=pk)
    form = PartnerForm()
    review = None
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.save()
            review = Review.objects.create(partner=partner)
            return redirect('partners')
    context = {'form':form, 'product' : product, 'review' : review, 'group':group}
    return render(request,'productTry.html', context)

@login_required
def updateReview(request, pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES ,instance=review)
        if form.is_valid():
            form.save()
            return redirect('partners')
        
    context = {'form':form, 'review':review}
    return render(request, 'reviewForm.html', context)

@login_required
def updatePartner(request, pk):
    partner = Partner.objects.get(id=pk)
    form = PartnerUpdateForm(instance=partner)
    if request.method == 'POST':
        form = PartnerUpdateForm(request.POST, request.FILES ,instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partners')
        
    context = {'form':form, 'partner':partner}
    return render(request, 'partnerForm.html', context)

@login_required
def product(request,pk):
    product = Product.objects.get(ref=pk)
    partners = Partner.objects.filter(product=product)
    seen = False
    if partners.exists():
        for p in partners:
            if(p.status == 'Approved'):
                seen = True
                break
    reviews = None
    reviews = Review.objects.filter(partner__in=partners, submit='Submitted')
    context = {'product' : product, 'partners':partners,'reviews':reviews, 'seen':seen }
    return render(request,'product.html', context)

@login_required
def partnerProfile(request,pk):
    user = User.objects.get(username=pk)
    profile = Profile.objects.get(user=user)
    context = {'profile':profile}
    return render(request,'partnerProfile.html', context)

@login_required
def home(request):
    return render(request,'login.html')
