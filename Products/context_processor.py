from django.shortcuts import render
from Products.models import Category

def navbar_data(request):
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
    return {"category": category, "carousel": carousel, "mainsection": mainsection}
    