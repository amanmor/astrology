from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.


def home(request):
    blogg=Article.objects.all()
    return render(request,"index.html",{"blogg":blogg})

def blog(request):
    blogg=Article.objects.all()
    return render(request,"section/blog.html",{"blogg":blogg})

def return_policy(request):
    return render(request,"section/footer/return.html")

def terms_condition(request):
    return render(request,"section/footer/terms.html")

def privacy_policy(request):
    return render(request,"section/footer/privacy.html")



# Blog and Article
def blog_detail(request, pk):
    blog = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})


# Product
def product_list(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'product/product.html', {'products': products})



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return JsonResponse({"message": "Added to cart!"})