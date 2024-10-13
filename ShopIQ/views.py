from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    category = [
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/698ba0cebe456aaf.jpg?q=100", "name": "Top Offer"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/4da1d0d19350cc84.jpg?q=100", "name": "Electronics"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/9d4e9c605fc1d2d3.jpg?q=100", "name": "Fashion"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/44e10b16e649b691.jpg?q=100", "name": "Mobiles"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/a5e656672d0548dd.jpg?q=100", "name": "Beauty"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/5b813b64a3179898.jpg?q=100", "name": "Home"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/7a5e96c10ada8a56.jpg?q=100", "name": "Furniture"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/57fe1ffe54569c41.jpg?q=100", "name": "Travel"},
        {"img": "https://rukminim2.flixcart.com/fk-p-flap/64/64/image/25f400c36bc3487d.jpg?q=100", "name": "Grocery"},
    ]
    carousel = [{"img":"https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/a1446c3eec72dee4.jpeg?q=20","redirect_to":"someurl"},
                {"img":"https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/0e03659c089a3055.jpg?q=20","redirect_to":"someurl"},
                {"img":"https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/a1446c3eec72dee4.jpeg?q=20","redirect_to":"someurl"},
                {"img":"https://rukminim2.flixcart.com/fk-p-flap/1600/270/image/0e03659c089a3055.jpg?q=20","redirect_to":"someurl"}]
    items = [
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        {"img":"","price": 100,"name":"dell laptop"},
        ]
    mainsection = [{"heading": "top items","items": items},{"heading": "Trending","items": items},{"heading": "Currently Selled","items": items},{"heading": "For You","items": items}]
    context = {"category": category,"carousel":carousel,"mainsection":mainsection}
    return render(request, 'index.html', context)
