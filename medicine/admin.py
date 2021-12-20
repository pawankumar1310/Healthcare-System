from medicine.models import Manufacturer, Medicine
from django.contrib import admin
@admin.register(Manufacturer)
class ManufacturerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','contact_no']

@admin.register(Medicine)
class MedicineModelAdmin(admin.ModelAdmin):
    list_display = ['id','name_medicine','use_medicine','benefits_medicine','side_effects_medicine','safety_advice_medicine','subMedicine']
