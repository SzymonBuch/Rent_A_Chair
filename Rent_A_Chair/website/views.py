from django.shortcuts import render

from Rent_A_Chair_App.models import Storage, Worker, Product


def index(request):
    return render(request, "website/index.html")


def storage(request):
    return render(request, "website/storage.html", {"storages": Storage.objects.all()})


def worker(request):
    return render(request, "website/worker.html", {"workers": Worker.objects.all()})


def product(request):
    return render(request, "website/product.html", {"products": Product.objects.all()})