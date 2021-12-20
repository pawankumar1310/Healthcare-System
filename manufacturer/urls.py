# from django.urls import path
# from .views import ManufacturerView,ManufacturerDetail,AddManufacturerView
from . import views

# urlpatterns = [
# 	path('register/', views.user_signup, name='register'),
# 	path('changepassword/',views.user_password_changed,name='changepassword'),
# 	path('login/',views.user_login,name='login'),
# 	path('logout/', views.user_logout, name='logout'),

# 	path('profile', ManufacturerView.as_view(), name='profile'),
#     path('manufacturer/<int:pk>/', ManufacturerDetail.as_view(), name='manufacturer-details'),
#     path('add_manufacturer/', AddManufacturerView.as_view(), name='add_manufacturer'),
# ]

from .views import ManufacturerView,ManufacturerDetail,AddManufacturerView
from django.urls import path
from .views import userlogout,userregister

urlpatterns = [
	path('register/', userregister.register, name='register'),
    path('login/', views.userlogin.as_view(), name='login'),
	path('changepassword/',views.PasswordChanged.as_view(),name='changepassword'),
	path('logout/', userlogout.logout_user, name='logout'),
	path('profile', ManufacturerView.as_view(), name='profile'),
    path('manufacturer/<int:pk>/', ManufacturerDetail.as_view(), name='manufacturer-details'),
    path('add_manufacturer/', AddManufacturerView.as_view(), name='add_manufacturer'),
]
