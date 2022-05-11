from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.http import HttpResponse

from .models import Product, Worker, Storage
import csv, datetime


ProductForm = modelform_factory(Product, exclude=[])
WorkerForm = modelform_factory(Worker, exclude=[])
StorageForm = modelform_factory(Storage, exclude=[])


def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product")
    else:
        form = ProductForm()
    return render(request, "website/new_product.html", {"form": form})


def new_storage(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("storage")
    else:
        form = StorageForm()
    return render(request, "website/new_storage.html", {"form": form})


def new_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("worker")
    else:
        form = WorkerForm()
    return render(request, "website/new_worker.html", {"form": form})


def product_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename=Products' + \
                                      str(datetime.datetime.now()) +'.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', "Amount", 'Storage'])

    products = Product.objects.filter()

    for product in products:
        writer.writerow([product.name, product.price, product.amount, product.storage_id.name])

    return response


