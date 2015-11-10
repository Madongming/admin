from django.shortcuts import render
from django.http import JsonResponse
from visualization.elasticsedata import *
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
#from myuser.models import *

# Create your views here.

def index(request):
#    monitor_names = {}
#    dashboard_infos = User.objects.get(id=request.user.userid).dashboard
#    for dashboard_info in dashboard_info.split(';'):
#        monitor_names[dashboard_info[1]] = Search_data.objects.get(id=int(str(dashboard_info[3:]))).monitor_name
#    if dashboard_infos[0] == '1':
#        return render(request, 'dashboard1_user.html', {'monitor_names': monitor_names})
#    if dashboard_infos[0] == '2':
#        return render(request, 'dashboard2_user.html', {'monitor_names': monitor_names})
#    else:
#        return render(request, 'index.html')
    return render(request, 'index.html')

def product_count(request):
    return render(request, 'temp_for_gen.html', {'monitor_names': Search_data.objects.get(id=29).monitor_name})

def order_count(request):
    return render(request, 'temp_for_gen.html', {'monitor_names': Search_data.objects.get(id=30).monitor_name})

def money_of_province(request):
    return render(request, 'money_of_province.html')

def money_of_all(request):
    return render(request, 'temp_for_gen.html', {'monitor_names': Search_data.objects.get(id=31).monitor_name})

def site_data(request):
    return render(request, 'temp_for_gen.html', {'monitor_names': Search_data.objects.get(id=32).monitor_name})

def busniss_data(request):
    return render(request, 'temp_for_gen.html', {'monitor_names': Search_data.objects.get(id=33).monitor_name})

def base_monitor(request):
    limit = 15
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
    return HttpResponse(json.dumps(es.getPicJson(**results), ensure_ascii=False ))

def api_post_profile_data_test(request):
    results = dict(request.POST.iterlists())
    for key in results:
        results[key] = results[key][0]
    es=getElastseData()
    return HttpResponse(json.dumps(es.getPicJson_test(**results), ensure_ascii=False ))

def api_post_get_city_data(request):
    results = dict(request.POST.iterlists())
    city_id = results['city_id'][0]
    city_data = int(random.uniform(10000,200000))
    return HttpResponse(json.dumps({'data':city_data}, ensure_ascii=False ))

def api_post_get_source_data(request):
    results = dict(request.POST.iterlists())
    for key in results:
        results[key] = results[key][0]
    es=getElastseData()
    return HttpResponse(json.dumps(es.getResult(**results), ensure_ascii=False ))

def database_monitor(request):
    limit = 15
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
    monitor_names = {}
    dashboard_infos = User.objects.get(id=request.user.userid).dashboard
    for dashboard_info in dashboard_info.split(';'):
        monitor_names[dashboard_info[1]] = Search_data.objects.get(id=int(str(dashboard_info[3:]))).monitor_name
    return render(request, 'dashboard2.html', {'monitor_names': monitor_names})
