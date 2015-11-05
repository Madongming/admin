from django.shortcuts import render
from django.http import JsonResponse
from visualization.elasticsedata import *
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_count(request):
    return render(request, 'product_count.html')

def order_count(request):
    return render(request, 'order_count.html')

def money_of_province(request):
    return render(request, 'money_of_province.html')

def money_of_all(request):
    return render(request, 'money_of_all.html')

def site_data(request):
    return render(request, 'site_data.html')

def base_monitor(request):
    limit = 5
    monitor_name = []
    for obj in Search_data.objects.all():
        monitor_name.append(obj.monitor_name)
    paginator = Paginator(monitor_name, limit)
    page = request.GET.get('page')
    try:
        monitor_name = paginator.page(page)
    except PageNotAnInteger:
        monitor_name = paginator.page(1)
    except EmptyPage:
        monitor_name = paginator.page(paginator.num_pages)
    return render(request, 'base_monitor.html', {'monitor_names': monitor_name})

def api_post_profile_data(request):
    results = dict(request.POST.iterlists())
    for key in results:
        results[key] = results[key][0]
    es=getElastseData()
    print es.getPicJson(**results)
    return HttpResponse(json.dumps(es.getPicJson(**results), ensure_ascii=False ))

def database_monitor(request):
    limit = 5
    monitor_name = []
    for obj in Search_data.objects.filter(monitor_name__icontains='mysql'):
        monitor_name.append(obj.monitor_name)
    paginator = Paginator(monitor_name, limit)
    page = request.GET.get('page')
    try:
        monitor_name = paginator.page(page)
    except PageNotAnInteger:
        monitor_name = paginator.page(1)
    except EmptyPage:
        monitor_name = paginator.page(paginator.num_pages)
    return render(request, 'database_monitor.html', {'monitor_names': monitor_name})

def dashboard1(request):
    monitor_names = {}
    for obj in Search_data.objects.filter(num_dashboard__startswith='1'):
        monitor_names[obj.num_dashboard[-1]] = obj.monitor_name
    return render(request, 'dashboard1.html', {'monitor_names': monitor_names})

def dashboard2(request):

    return render(request, 'dashboard2.html')

