from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.


class Device(models.Model):
    DEVICE_CHOICES = [
        ("Computer", "Computer"),
        ("PS3", "PS3"),
        ("PS4", "PS4"),
        ("PS5", "PS5"),
        ("X-BOX", "X-BOX"),
    ]

    PRICE_CHOICES = [
        ("CP_1h", 10000),
        ("PS3_1h", 30000),
        ("PS4_1h", 40000),
        ("PS5_1h", 50000),
        ("X-BOX_1h", 50000),
    ]

    device_type = models.CharField(max_length=9, choices=DEVICE_CHOICES, default="Computer")
    device_name = models.CharField(max_length=10)
    price = models.CharField(max_length=9, choices=PRICE_CHOICES, default="CP_1h")

    def __str__(self):
        return self.device_name


class Gamer(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name


class RentedDevice(models.Model):
    device_type = models.ForeignKey(Device, on_delete=SET_NULL, blank=True, null=True)
    gamer = models.ForeignKey(Gamer, on_delete=SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    # def __str__(self):
    #     return self.start_time


class BookCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


# class Book1Category(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.TextField(null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Profile(models.Model):
#     BookCategory = models.ManyToManyField(BookCategory)
#     Book1Category = models.ManyToManyField(Book1Category)
#
#
# class AccessKey(models.Model):
#     key = models.CharField(max_length=100)

