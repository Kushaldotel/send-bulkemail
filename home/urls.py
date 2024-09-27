from django.urls import path
from .views import home,services,contact,service_detail,aboutus

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('services/',services,name='services'),
    path('service/<slug:slug>/', service_detail, name='service_detail'),
    path('contact-us/', contact,name='contactus')
]
