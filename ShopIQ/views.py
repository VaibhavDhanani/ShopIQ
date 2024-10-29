from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Products.models import *
from django.utils import timezone
from django.db.models import Prefetch


def index(request):
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

    sections_data = []

    active_sections = (
        Section.objects.filter(is_active=True)
        .exclude(
            models.Q(start_date__gt=timezone.now())
            | models.Q(end_date__lt=timezone.now())
        )
        .prefetch_related(
            Prefetch(
                "section_products",
                queryset=SectionProduct.objects.select_related("product").order_by(
                    "display_order", "-added_date"
                ),
            )
        )
    )

    for section in active_sections:
        products = [sp.product for sp in section.section_products.all()]

        if products:
            sections_data.append(
                {
                    "title": section.name,
                    "products": products,
                    "bgcolor": section.background_color,
                }
            )

    context = {"carousel": carousel, "mainsection": sections_data}
    return render(request, "index.html", context)
