from django.shortcuts import render, redirect
from django.forms import modelform_factory

from .models import Product, Worker, Storage


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
# Create your views here.
