from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=True)
    address = models.TextField(null=True, blank=True)
    contact_no = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
	    return reverse('home')
