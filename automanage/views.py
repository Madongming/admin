from django.shortcuts import render

# Create your views here.

def add_host(request):
    return render(request, 'add_host.html')

def delete_host(request):
    return render(request, 'delete_host.html')

def add_service(request):
    return render(request, 'add_service.html')

def delete_service(request):
    return render(request, 'delete_service.html')
