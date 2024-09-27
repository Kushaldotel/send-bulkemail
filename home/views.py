from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Services

# Create your views here.
def home(request):

    services = Services.objects.all()
    context = {
        'services': services
    }

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,  # Email subject
            message,  # Email message
            settings.DEFAULT_FROM_EMAIL,  # From email
            [settings.DEFAULT_FROM_EMAIL],  # To email (can be admin email or any recipient)
            fail_silently=False,
        )
        return redirect('home')

    return render(request, 'home/base.html', context)

def aboutus(request):
    return render(request,'home/aboutus.html')

def services(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request,'home/services.html',context)

def service_detail(request, slug):
    service = get_object_or_404(Services, slug=slug)
    return render(request, 'home/services-detail.html', {'service': service})

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,  # Email subject
            message,  # Email message
            settings.DEFAULT_FROM_EMAIL,  # From email
            [settings.DEFAULT_FROM_EMAIL],  # To email (can be admin email or any recipient)
            fail_silently=False,
        )
        return redirect('contactus')
    return render(request,'home/contactus.html')