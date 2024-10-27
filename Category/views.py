from django.shortcuts import render, get_object_or_404
from .models import Category
from Products.models import Product

def ShowCategoryWiseProducts(request, catslug):
    category = get_object_or_404(Category, slug=catslug)
    products = Product.objects.filter(categories=category)
    return render(request, "category_detail.html", {"category": category, "products": products})

def ShowAllCategoryWiseProducts(request):
    categories = Category.objects.all()
    all_products_by_category = {category: Product.objects.filter(categories=category) for category in categories}
    return render(request, "all_categories.html", {"all_products_by_category": all_products_by_category})
