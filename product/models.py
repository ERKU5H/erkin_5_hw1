from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tag = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.title} - цена продукта {self.price}"


class Review(models.Model):
    text = models.CharField(max_length=100)
    stars = models.IntegerField(default=1, choices=[(i, i * "*") for i in range(1, 6)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=100)
