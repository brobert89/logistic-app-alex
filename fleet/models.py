from django.db import models

class Fleet(models.Model):
    fleet_number = models.CharField(max_length=50, unique=True)
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.fleet_number

class Order(models.Model):
    date = models.DateField()
    order_id = models.CharField(max_length=50, unique=True)
    trailer_number = models.CharField(max_length=50)
    pickup_address = models.TextField(blank=True, null=True)
    unload_address = models.TextField(blank=True, null=True)
    unload_time = models.TimeField(blank=True, null=True)
    load_address = models.TextField(blank=True, null=True)
    load_time = models.TimeField(blank=True, null=True)
    drop_off_address = models.TextField(blank=True, null=True)
    km_maps = models.FloatField(blank=True, null=True)
    waiting_time = models.FloatField(blank=True, null=True)
    fleet = models.ForeignKey(Fleet, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.order_id