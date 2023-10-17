from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'furni-1.0.0/index.html')
def about(request):
    return render(request, 'furni-1.0.0/about.html')
def shop(request):
    return render(request, 'furni-1.0.0/shop.html')
def services(request):
    return render(request, 'furni-1.0.0/services.html')
def contact(request):
    return render(request, 'furni-1.0.0/contact.html')
def sesion(request):
    return render(request, 'furni-1.0.0/sesion.html')
