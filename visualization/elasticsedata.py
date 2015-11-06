#!/usr/bin/env python

#coding: utf-8

from visualization.elasticsedata_base import *
from visualization.models import *
#from elasticsedata_base import *
#from models import *
from django.forms.models import model_to_dict
from string import Template
from django.conf import settings
import datetime

####for test data###
import random
####for test data###

class getElastseData(ElastseData):
    def getData(self, **kw):
        index = kw.get('index')
        query = kw.get('query', None)
        time_start = kw.get('time_start')
        time_end = kw.get('time_end')
        interval = kw.get('interval', None) 
        fields = kw.get('fields', None)
        if fields is not None:
            fields = fields.split(';')
            while '' in fields:
                fields.remove('')
        field = kw.get('field', None)
        name = kw.get('name', None)
        size = kw.get('size', None)
        sub_fields = kw.get('sub_fields', None)
        if sub_fields is not None:
            sub_fields = sub_fields.split(';')
            while '' in sub_fields:
                sub_fields.remove('')
        mothod_type = kw.get('mothod_type', None)
        if mothod_type == 'gen':
            return self._formatData_gen(self._getData_gen(index=index, query=query, time_start=time_start, time_end=time_end, interval=interval, fields=fields), fields=fields)
        if mothod_type == 'per_sum':
            return self._formatData_some_per_sum(self._getData_some_per_sum(index=index, time_start=time_start, time_end=time_end, interval=interval, field=field), name=name)
        if mothod_type == 'sum':
            return self._formatData_some_sum(self._getData_some_sum(index=index, time_start=time_start, time_end=time_end, field=field), name=name)
        if mothod_type == 'cardinality':
            return self._formatData_cardinality(self._getData_cardinality(index=index, time_start=time_start, time_end=time_end, interval=interval, field=field), name=name)
        if mothod_type == 'count':
            return self._formatData_count(self._getData_count(index=index, query=query, time_start=time_start, time_end=time_end, interval=interval), name=name)
        if mothod_type == 'some_top':
            return self._formatData_some_top(self._getData_some_top(index=index, time_start=time_start, time_end=time_end, field=field, size=size))
        if mothod_type == 'sub_query':
            return self._formatData_has_sub_query(self._getData_has_sub_query(index=index, time_start=time_start, time_end=time_end, interval=interval, field=field, sub_fields=sub_fields),field=field)
        if mothod_type == 'sub_sum':
            return self._formatData_has_sub_sum(self._getData_has_sub_sum(index=index, query=query, time_start=time_start, time_end=time_end, interval=interval, fields=fields),fields=fields)

    def getResult(self, **kw):
        monitor_name = kw.get('monitor_name', None)
        if monitor_name is not None:
            pro_data = model_to_dict(Search_data.objects.get(monitor_name=monitor_name))
            pro_data['index'] = '%s-%s' % (pro_data['index'], time.strftime('%Y.%m.%d',time.localtime(time.time())))
        pro_data['time_start'] = int(kw.get('time_start'))
        pro_data['time_end'] = int(kw.get('time_end'))
        pro_data['interval'] = kw.get('interval')
        try:
            return self.getData(**pro_data)
        except:
            return 'Get profile ERROR!'

    def getPicJson(self, **kw):
        monitor_name = kw.get('monitor_name', None)
        if monitor_name is not None:
            data = model_to_dict(Search_data.objects.get(monitor_name=monitor_name))
        data['time_start'] = int(kw.get('time_start'))
        data['time_end'] = int(kw.get('time_end'))
        data['interval'] = kw.get('interval')
        time_start_date = int(datetime.datetime.fromtimestamp(data['time_start']/1000).strftime('%d'))
        time_end_date = int(datetime.datetime.fromtimestamp(data['time_end']/1000).strftime('%d'))
        if time_start_date != time_end_date:
            index_list = []
            for i in range(data['time_start']/1000, data['time_end']/1000, 86400):
                index_list.append('%s-%s' % (data['index'],datetime.datetime.fromtimestamp(i).strftime('%Y.%m.%d')))
            data['index'] = ','.join(index_list)
        else:
            data['index'] = '%s-%s' % (data['index'], datetime.datetime.fromtimestamp(data['time_end']/1000).strftime('%Y.%m.%d'))
        results = self.getData(**data)
        if data['pic_type'] == 'line':
            filepath = '%s/visualization/templates/json/chart_template.json' % settings.BASE_DIR
        elif data['pic_type'] == 'column':
            filepath = '%s/visualization/templates/json/chart_column_template.json' % settings.BASE_DIR
        with open(filepath, 'r') as f:
            tempstr = f.read()
        tempstr = tempstr.replace('\n','').replace(' ','').decode()
        CHART_TYPE = data['pic_type']
        TITLE_TEXT = data['monitor_name']
        interval = data['interval']
        if interval[-1] == 's':
            per = int(interval[0:-1])
#            fn = lambda x:time.strftime('%H:%M:%S',time.localtime(float(x)))
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H:%M:%S')
        if interval[-1] == 'm':
            per=int(interval[0:-1]) * 60
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H:%M')
        if interval[-1] == 'h':
            per=int(interval[0:-1]) * 60 * 60
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H')
        if interval[-1] == 'w':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 7
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%w')
        if interval[-1] == 'M':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 30
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%m')
        if interval[-1] == 'y':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 365
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%Y')
        start = data['time_start'] / 1000
        end = data['time_end'] / 1000
        if data['pic_type'] == 'line':
            XAXIS_CATEGORIES = str(map(fn,range(start, end+per, per)))
            SERIES_LIST_NAME_DATA_DICT = []
            for key in results:
                SERIES_LIST_NAME_DATA_DICT.append({'name':key.encode(), 'data':results[key]})
            tempdict = {u'CHART_TYPE':u"'"+CHART_TYPE+u"'", u'TITLE_TEXT':u"'"+TITLE_TEXT+u"'", u'XAXIS_CATEGORIES':XAXIS_CATEGORIES, u'TOOLTIP_ENABLED':False, u'PLOTOPTIONS_LINE_DATALABELS_ENABLED':True, u'PLOTOPTIONS_LINE_ENABLEMOUSETRACKING':False, u'SERIES_LIST_NAME_DATA_DICT':SERIES_LIST_NAME_DATA_DICT}
        elif data['pic_type'] == 'column':
            XAXIS_CATEGORIES = []
            SERIES_DATA = []
            SERIES_NAME = data['field']
            for key in results:
                XAXIS_CATEGORIES.append(key)
                SERIES_DATA.append(results[key])
            tempdict = {u'CHART_TYPE':u"'"+CHART_TYPE+u"'", u'TITLE_TEXT':u"'"+TITLE_TEXT+u"'", u'XAXIS_CATEGORIES':XAXIS_CATEGORIES, 'SERIES_NAME':u"'"+SERIES_NAME+"'", 'SERIES_DATA':SERIES_DATA}
        return json.dumps(Template(tempstr).substitute(tempdict))

    def getPicJson_test(self, **kw):
        monitor_name = kw.get('monitor_name', None)
        if monitor_name is not None:
            data = model_to_dict(Search_data.objects.get(monitor_name=monitor_name))
        data['time_start'] = int(kw.get('time_start'))
        data['time_end'] = int(kw.get('time_end'))
        data['interval'] = kw.get('interval')
        time_start_date = int(datetime.datetime.fromtimestamp(data['time_start']/1000).strftime('%d'))
        time_end_date = int(datetime.datetime.fromtimestamp(data['time_end']/1000).strftime('%d'))
        if time_start_date != time_end_date:
            index_list = []
            for i in range(data['time_start']/1000, data['time_end']/1000, 86400):
                index_list.append('%s-%s' % (data['index'],datetime.datetime.fromtimestamp(i).strftime('%Y.%m.%d')))
            data['index'] = ','.join(index_list)
        else:
            data['index'] = '%s-%s' % (data['index'], datetime.datetime.fromtimestamp(data['time_end']/1000).strftime('%Y.%m.%d'))


        a = data['time_start'] / 1000
        b = data['time_end'] / 1000
        interval = data['interval']
        if interval[-1] == 's':
            per = int(interval[0:-1])
        if interval[-1] == 'm':
            per=int(interval[0:-1]) * 60
        if interval[-1] == 'h':
            per=int(interval[0:-1]) * 60 * 60
        if interval[-1] == 'w':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 7
        if interval[-1] == 'M':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 30
        if interval[-1] == 'y':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 365
        c = per

        columns = data['fields'].split(';')
        while '' in columns:
            columns.remove('')
        results = {}
        for key in columns:
            results[key] = []
        for key in results:
            d = (b-a+c)/c
            while d:
                results[key].append(int(random.uniform(10000,200000)))
                d -= 1
                

        if data['mothod_type'] == 'gen':
            filepath = '%s/visualization/templates/json/chart_template.json' % settings.BASE_DIR
        elif data['mothod_type'] == 'some_top':
            filepath = '%s/visualization/templates/json/chart_column_template.json' % settings.BASE_DIR
        with open(filepath, 'r') as f:
            tempstr = f.read()
        tempstr = tempstr.replace('\n','').replace(' ','').decode()
        CHART_TYPE = data['pic_type']
        TITLE_TEXT = data['monitor_name']
        interval = data['interval']
        if interval[-1] == 's':
            per = int(interval[0:-1])
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H:%M:%S')
        if interval[-1] == 'm':
            per=int(interval[0:-1]) * 60
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H:%M')
        if interval[-1] == 'h':
            per=int(interval[0:-1]) * 60 * 60
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%H')
        if interval[-1] == 'w':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 7
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%w')
        if interval[-1] == 'M':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 30
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%m')
        if interval[-1] == 'y':
            per=int(interval[0:-1]) * 60 * 60 * 24 * 365
            fn = lambda x:datetime.datetime.fromtimestamp(x).strftime('%Y')
        start = data['time_start'] / 1000
        end = data['time_end'] / 1000
        if data['mothod_type'] == 'gen':
            XAXIS_CATEGORIES = str(map(fn,range(start, end+per, per)))
            SERIES_LIST_NAME_DATA_DICT = []
            for key in results:
                SERIES_LIST_NAME_DATA_DICT.append({'name':key.encode(), 'data':results[key]})
            tempdict = {u'CHART_TYPE':u"'"+CHART_TYPE+u"'", u'TITLE_TEXT':u"'"+TITLE_TEXT+u"'", u'XAXIS_CATEGORIES':XAXIS_CATEGORIES, u'TOOLTIP_ENABLED':False, u'PLOTOPTIONS_LINE_DATALABELS_ENABLED':True, u'PLOTOPTIONS_LINE_ENABLEMOUSETRACKING':False, u'SERIES_LIST_NAME_DATA_DICT':SERIES_LIST_NAME_DATA_DICT}
        elif data['mothod_type'] == 'some_top':
            XAXIS_CATEGORIES = []
            SERIES_DATA = []
            SERIES_NAME = data['field']
            for key in results:
                XAXIS_CATEGORIES.append(key)
                SERIES_DATA.append(results[key])
            tempdict = {u'CHART_TYPE':u"'"+CHART_TYPE+u"'", u'TITLE_TEXT':u"'"+TITLE_TEXT+u"'", u'XAXIS_CATEGORIES':XAXIS_CATEGORIES, 'SERIES_NAME':u"'"+SERIES_NAME+"'", 'SERIES_DATA':SERIES_DATA}
        return json.dumps(Template(tempstr).substitute(tempdict))

if __name__ == '__main__':
    es=getElastseData()
    now = int(time.time()*1000)
    kw = {u'monitor_name': u'Nginx uv', u'time_start':now, u'time_end':now-900000, u'interval':'30s'}
    es.getResult(**kw)
