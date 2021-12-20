from django.shortcuts import render,HttpResponseRedirect,HttpResponse, redirect, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import ChangePassword
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.views import View
from django.views.generic import ListView, DetailView,CreateView
from .models import Manufacturer
from .forms import ManufacturerForm

# def user_signup(request):
#  if request.method == "POST":
#   form = SignUpForm(request.POST)
#   if form.is_valid():
#    user = form.save()
#  else:
#   form = SignUpForm()
#  return render(request, 'register.html', {'form':form})


class userregister(View):
    def register(request):
        if request.user.is_authenticated:
            return redirect('base')
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Register Successfully !!')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form':form})

# def user_login(request):
#  if not request.user.is_authenticated:
#   if request.method == "POST":
#    form = LoginForm(request=request, data=request.POST)
#    if form.is_valid():
#     uname = form.cleaned_data['username']
#     upassword = form.cleaned_data['password']
#     user = authenticate(username=uname, password=upassword)
#     if user is not None:
#      login(request, user)
#      messages.success(request, 'Logged in Successfully !!')
#      return HttpResponseRedirect('/')
#   else:
#    form = LoginForm()
#   return render(request, 'login.html', {'form':form})
#  else:
#   return HttpResponseRedirect('/')

class userlogin(View):
    def get(self,request):
        form = LoginForm()
        if(request.user.is_authenticated):
            return redirect('/')
        return render(request, 'login.html',{'form':form})

    def post(self,request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return redirect('/')
                else:
                    return render(request,'login.html',{'error_message': 'Your account has not been activated!'})
            else:
                return render(request,'login.html', {'error_message': 'Invalid login'})
        return render(request, 'login.html', {'form':form})



# def user_logout(request):
#  logout(request)
#  return HttpResponseRedirect('/')

class userlogout(View):
    def logout_user(request):
        logout(request)
        return redirect('/')

# def user_password_changed(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = ChangePassword(user=request.user,data = request.POST)
#             if fm.is_valid():
#                 fm.save()
#                 update_session_auth_hash(request,fm.user)
#                 messages.success(request,'Password changed Successfully!')
#         else:
#             fm=ChangePassword(user=request.user)
#         return render(request,'changepass.html',{'form':fm})
#     else:
#         return HttpResponseRedirect('/login/')
class PasswordChanged(View):
    def get(self,request):
        form = ChangePassword(user=request.user)
        if(not request.user.is_authenticated):
            return redirect('/')
        return render(request, 'changepass.html',{'form':form})

    def post(self,request):
        form = ChangePassword(user=request.user,data = request.POST)
        if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed Successfully!')
        return render(request,'changepass.html',{'form':form})

class ManufacturerView(ListView):
	model = Manufacturer
	template_name = 'profile.html'
	success_message = 'Successfully saved!!!!'

class ManufacturerDetail(DetailView):
	model = Manufacturer
	template_name = 'manufacturer_details.html'


class AddManufacturerView(CreateView):
	model = Manufacturer
	form_class = ManufacturerForm
	template_name = 'add_manufacturer.html'

