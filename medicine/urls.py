from medicine.models import Medicine
from django.urls import path
from . import views
from medicine.views import HomeView, MedicineDetail,AddMedicineView,MedicineSearchView,autosuggest

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
    path('add_medicine/', AddMedicineView.as_view(), name='add_medicine'),
    path('search/',MedicineSearchView.as_view(),name='search'),
    path('autosuggest/',autosuggest,name='autosuggest'),
]