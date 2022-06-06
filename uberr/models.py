from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Destination(models.Model):
    address = models.CharField(max_length=200)
    order_date = models.DateTimeField('date of order')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

