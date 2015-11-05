from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from visualization.models import *
from django.forms.models import model_to_dict
import json
# Create your views here.

def conf_dashboard(request):
    return render(request, 'conf_dashboard.html')

def manage_pic(request):
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
    return render(request, 'manage_pic.html', {'monitor_names': monitor_name})

def post_get_profile_data(request):
    modify_name = dict(request.POST.iterlists())
    result = model_to_dict(Search_data.objects.get(monitor_name=modify_name['monitor_name'][0]))
    return HttpResponse(json.dumps(result, ensure_ascii=False ))

def post_update_pic_profile(request):
    data = dict(request.POST.iterlists())
    for key in data:
        data[key] = data[key][0]
    update_row = Search_data.objects.get(id=int(data['id']))
    for key in data:
        update_row.key = data[key]
    return HttpResponse(json.dumps(update_row.save()))
