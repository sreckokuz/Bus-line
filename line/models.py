from django.db import models

# Create your models here.


class Line(models.Model):
    name = models.CharField(max_length=30)
    line_number = models.IntegerField()

    def __str__(self):
        return self.name


class Station(models.Model):
    lat = models.DecimalField(decimal_places=4, max_digits=10)
    lng = models.DecimalField(decimal_places=4, max_digits=10)
    station_name = models.CharField(max_length=30)

    def __str__(self):
        return self.station_name
