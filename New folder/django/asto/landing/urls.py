from django.urls import path
from .views import home,blog,return_policy,terms_condition,privacy_policy,blog_detail,product_list,add_to_cart
urlpatterns = [
    path('',home,name="home"),
    path('blog',blog,name="blog"),
    path('return',return_policy,name="return_policy"),
    path('terms',terms_condition,name="terms_condition"),
    path('privacy',privacy_policy,name="privacy_policy"),
    path('blog/<int:pk>/', blog_detail, name='detail'),
    path('products/<str:category>/', product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]

