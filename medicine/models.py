from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from manufacturer.models import Manufacturer



class Medicine(models.Model):
    manufactured_by = models.ForeignKey(Manufacturer, null=True, on_delete=models.CASCADE)
    name_medicine = models.CharField(max_length=255)
    price_medicine = models.FloatField(blank=True)
    use_medicine = models.TextField(null=True, blank=True)
    benefits_medicine = models.TextField(null=True, blank=True)
    side_effects_medicine = models.TextField(null=True, blank=True)
    safety_advice_medicine = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to="images/", null=True, blank=True)
    substitute = models.ManyToManyField("self")


    def get_absolute_url(self):
	    return reverse('home')
    class Meta:
        ordering = ['name_medicine']

    def __str__(self):
        return self.name_medicine

    def subMedicine(self):
        return ", ".join([str(p) for p in self.substitute.all()])
    








