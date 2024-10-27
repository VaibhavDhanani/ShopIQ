from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Products.models import Product, Category


def index(request):

# Filter and remove products with invalid category references
    invalid_products = Product.objects.filter(categories__isnull=True)
    invalid_products.delete()

    category = Category.objects.filter(parent__isnull=True)
    print(category)
    carousel = [
        {
            "img": "https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/a1446c3eec72dee4.jpeg?q=20",
            "redirect_to": "someurl",
        },
        {
            "img": "https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/0e03659c089a3055.jpg?q=20",
            "redirect_to": "someurl",
        },
        {
            "img": "https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/a1446c3eec72dee4.jpeg?q=20",
            "redirect_to": "someurl",
        },
        {
            "img": "https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/0e03659c089a3055.jpg?q=20",
            "redirect_to": "someurl",
        },
    ]
    items = [
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
        {"img": "", "price": 100, "name": "dell laptop"},
    ]

    mainsection = [
        {"heading": "top items", "items": items},
        {"heading": "Trending", "items": items},
        {"heading": "Currently Selled", "items": items},
        {"heading": "For You", "items": items},
    ]
    context = {"category": category, "carousel": carousel, "mainsection": mainsection}
    return render(request, "index.html", context)




