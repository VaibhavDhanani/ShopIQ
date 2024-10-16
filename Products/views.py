from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product,Category


def getAllProduct(request):
    dummy = Category.objects.all()
    products = Product.objects.all()
    print(dummy,products)
    context = {"products": products}
    return render(request, "product-panel.html", context)


def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-products")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "product-update.html", context)


def updateProduct(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("all-products")
    else:
        form = ProductForm(instance=product)
    context = {"form": form}
    return render(request, "product-update.html", context)


def deleteProduct(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        product.delete()
        return redirect("all-products")
    context = {"product": product}
    return render(request, "product-delete.html", context)
