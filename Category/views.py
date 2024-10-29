from django.shortcuts import render, get_object_or_404
from .models import Category
from Products.models import Product


def ShowCategoryWiseProducts(request, catslug):
    category = Category.objects.get(slug=catslug)
    products_of_category = Product.objects.filter(categories=category)
    section = {"title": category.name, "products": products_of_category}
    context = {"section": section}
    return render(request, "category_detail.html", context)


def ShowAllCategoryWiseProducts(request):
    categories = Category.objects.all()
    all_products_by_category = {
        category: Product.objects.filter(categories=category) for category in categories
    }
    return render(
        request,
        "all_categories.html",
        {"all_products_by_category": all_products_by_category},
    )
