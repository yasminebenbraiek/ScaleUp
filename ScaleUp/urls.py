from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('product/', views.products, name="products"),
    path('product/<str:pk>/', views.product, name="product"),
    path('product-try/<str:pk>/', views.productTry, name="productTry"),
    path('product-create/', views.createProduct, name="createProduct"),
    path('product-update/<str:pk>/', views.updateProduct, name="updateProduct"),
    path('product-delete/<str:pk>/', views.deleteProduct, name="deleteProduct"),
    path('profile/', views.profile, name="profile"),
    path('profile-update/', views.updateProfile, name="updateProfile"),
    path('post/', views.posts, name="posts"),
    path('post-create', views.createPost, name="createPost"),
    path('post-update/<int:pk>/', views.updatePost, name="updatePost"),
    path('post-delete/<int:pk>/', views.deletePost, name="deletePost"),
    path('partner/', views.partners, name="partners"),
    path('partner-profile/<str:pk>/', views.partnerProfile, name="partnerProfile"),
    path('partner-review/<int:pk>/', views.updateReview, name="updateReview"),
    path('partner-update/<int:pk>/', views.updatePartner, name="updatePartner"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


