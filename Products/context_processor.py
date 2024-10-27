from django.shortcuts import render
from Products.models import Category

def navbar_data(request):
    category = Category.objects.filter(parent__isnull=True)
    return {"category": category}
    