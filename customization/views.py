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
    monitor_names = []
    for obj in Search_data.objects.all():
        monitor_names.append(obj.monitor_name)
    return render(request, 'conf_dashboard.html', {'monitor_names': monitor_names})

def manage_pic(request):
    limit = 10
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
        if data[key] == 'null':
            data[key] = None
        setattr(update_row, key, data[key])
    status = True
    try:
        update_row.save()
    except:
        status = False
    return HttpResponse(json.dumps(status))

def post_create_pic_profile(request):
    data = dict(request.POST.iterlists())
    for key in data:
        data[key] = data[key][0]
    create_row = Search_data()
    for key in data:
        if data[key] == 'null' or data[key] == 'NULL' or data[key] == '':
            data[key] = None
        setattr(create_row, key, data[key])
    status = True
    try:
        create_row.save()
    except:
        status = False
    return HttpResponse(json.dumps(status))

def post_delete_pic_profile(request):
    data = dict(request.POST.iterlists())
    data['id'] = data['id'][0]
    delete_row = Search_data.objects.get(id=int(data['id']))
    status = True
    try:
        delete_row.delete()
    except:
        status = False
    return HttpResponse(json.dumps(status))

def post_conf_dashboard(request):
    data = dict(request.POST.iterlists())
    results = {}
    if data.has_key('dashboard1[]'):
        for monitor_name in data['dashboard1[]']:
            results[monitor_name] = '1%s' % str(data['dashboard1[]'].index(monitor_name)+1)
    if data.has_key('dashboard2[]'):
        for monitor_name in data['dashboard2[]']:
            results[monitor_name] = '2%s' % str(data['dashboard2[]'].index(monitor_name)+1)
    status = True
    try:
        backup = {}
        if data.has_key('dashboard1[]'):
            for value in range(11,15):
                if Search_data.objects.filter(num_dashboard=str(value)):
                    backup[str(value)] = Search_data.objects.filter(num_dashboard=str(value))[0].id
            backup = {value:key for key, value in backup.items()}
            if backup:
                for key in backup:
                    Search_data.objects.filter(id=key).update(num_dashboard=None)
        if data.has_key('dashboard2[]'):
            for value in range(21,24):
                if Search_data.objects.filter(num_dashboard=str(value)):
                    backup[str(value)] = Search_data.objects.filter(num_dashboard=str(value))[0].id
            backup = {value:key for key, value in backup.items()}
            if backup:
                for key in backup:
                    Search_data.objects.filter(id=key).update(num_dashboard=None)

        for key in results:
            Search_data.objects.filter(monitor_name=key).update(num_dashboard=results[key])
    except:
        status = False
        if backup:
            for key in backup:
                Search_data.objects.filter(id=key).update(num_dashboard=backup[key])
    return HttpResponse(json.dumps(status))
    
