from django.core.paginator import Paginator
from django.http import FileResponse
from django.shortcuts import render, redirect

from Rent_A_Chair_App.models import Storage, Worker, Product


def index(request):
    return render(request, "website/index.html")


def storage(request):
    return render(request, "website/storage.html", {"storages": Storage.objects.all()})


def worker(request):
    return render(request, "website/worker.html", {"workers": Worker.objects.all()})


def product(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 1)

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request, "website/product.html", {"products": products})


def return_image(response):
    img = open('website/static/website/media/bc2.jpg', 'rb')

    response = FileResponse(img)

    return response
