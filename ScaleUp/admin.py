from django.contrib import admin

from .models import Product
from .models import Category
from .models import Profile
from .models import Partner
from .models import Review
from .models import Post

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Partner)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Post)