from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} - {self.storage_id.name}"
