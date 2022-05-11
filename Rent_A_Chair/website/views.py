from django.core.paginator import Paginator
from django.http import FileResponse
from django.shortcuts import render, redirect
from .filters import WorkerFilter

from Rent_A_Chair_App.models import Storage, Worker, Product


def index(request):
    return render(request, "website/index.html")


def storage(request):
    return render(request, "website/storage.html", {"storages": Storage.objects.all()})


def worker(request):
    workers = Worker.objects.all()
    my_filter = WorkerFilter(request.GET, queryset=workers)
    workers = my_filter.qs

    return render(request, "website/worker.html", {"workers": workers, "my_filter": my_filter})


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


def return_image2(response):
    img = open('website/static/website/media/denspacito.gif', 'rb')

    response = FileResponse(img)

    return response


def worker_image(response):
    img = open('website/static/website/media/worker.jpg', 'rb')

    response = FileResponse(img)

    return response


def storage_image(response):
    img = open('website/static/website/media/magazyn.jpg', 'rb')

    response = FileResponse(img)

    return response


def product_image(response):
    img = open('website/static/website/media/chair.jpg', 'rb')

    response = FileResponse(img)

    return response


def return_banger(response):
    audio = open('website/static/website/media/bangers/Bangerito.mp3', 'rb')

    response = FileResponse(audio)

    return response



