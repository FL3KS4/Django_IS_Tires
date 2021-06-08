"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('error',views.errorPage, name='ErrorPage'),
    path('customers/',views.customers, name='customers'),
    path('customer/edit_customer<int:cust_id>',views.edit_customer, name='edit_customer'),
    path('customer/addVehicle<int:cust_id>',views.addVehicle, name='add_vehicle'),
    path('deleteVehicle/<int:cust_id>',views.vehicleDelete, name='vehicleDelete'),
    path('customer/<int:cust_id>',views.customer, name='customer'),
    path('customers/add_customer_succesfull',views.add_customer_succesfull, name='add_customer_succesfull'),
    path('delete/<int:cust_id>', views.customerDelete, name='customerDelete'),
    path('vehicles/',views.vehicles, name='vehicles'),
    path('vehicle/<int:veh_id>',views.vehicle, name='vehicle'),
    path('vehicle/edit_vehicle<int:veh_id>',views.edit_vehicle, name='edit_vehicle'),
    path('workers/',views.workers, name='workers'),
    path('tires/',views.tires, name='tires'),
    path('tire/<int:pneu_id>',views.tire, name='tire'),
    path('tire/edit_tire/<int:pneu_id>',views.edit_tire, name='edit_tire'),
    path('deleteTire/<int:pneu_id>',views.tireDelete, name='tireDelete'),
    path('tires/add_Tire',views.add_tire, name='add_tire'),
    path('records/',views.records, name='records'),
    path('deleteRecord/<int:rec_id>',views.deleteRecord, name='deleteRecord'),
    path('addRecord/',views.add_record, name='add_record'),
    path('contacts/',views.contact, name='contacts'),
    path('addRecord/getCustomer/',views.getCustomer, name='getCustomer'),
    path('addRecord/add_record_success',views.add_record_success, name='add_record_success'),
    path('vehicle/delete_tire_veh<int:veh_id>',views.deleteTireFromVeh, name='delete_tire_veh'),
]
