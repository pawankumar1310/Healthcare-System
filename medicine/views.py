from django.db.models import query
from django.utils.decorators import method_decorator
import medicine
from typing import List
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Medicine
from .forms import MedicineForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class HomeView(ListView):
	model = Medicine
	paginate_by = 5
	template_name = 'home.html'
	success_message = 'List successfully saved!!!!'


class MedicineDetail(DetailView):
	model = Medicine
	template_name = 'medicine_details.html'


class AddMedicineView(CreateView):
	model = Medicine
	form_class = MedicineForm
	template_name = 'add_medicine.html'


class MedicineSearchView(ListView):
	model = Medicine
	template_name = 'home.html'
	def get_queryset(self):
		query = self.request.GET.get('query')
		return Medicine.objects.filter(name_medicine__icontains=query)

def autosuggest(request):
	query_original = request.GET.get('term')
	queryset = Medicine.objects.filter(name_medicine__icontains=query_original)
	m =[]
	m += [x.name_medicine for x in queryset]
	return JsonResponse(m,safe=False)