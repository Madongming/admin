#!/usr/bin/env python

#coding: utf-8

import time
from elasticsearch import Elasticsearch
import json

class ElastseData(object):
    def __init__(self, host='172.16.1.133', port=9200):
        self.es = Elasticsearch([{'host':host,'port':port}])

    def format_value(self, value):
        if value is None:
            return 0
        elif isinstance(value, float):
            return float("%.2f" % value)
        else:
            return value

    def _getData_gen(self, index, query, time_start, time_end, interval, fields):
        aggs = {}
        for field in fields:
            aggs[field] = {'avg': {"field": field}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": query,
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": {
                'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }
                        },
                    "aggs": aggs
                    }
                }
            })
        return self.es.search(index=index, body=body)

    def _getData_some_per_sum(self, index, time_start, time_end, interval, field):
        aggs = {'some_per_sum': {'sum': {'field': field}}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": '*',
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": {
                'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }
                        },
                    "aggs": aggs
                    }
                }
            })
        return self.es.search(index=index, body=body)

    def _getData_some_sum(self, index, time_start, time_end, field):
        aggs = {'some_sum': {'sum': {'field': field}}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": '*',
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": aggs
            })
        return self.es.search(index=index, body=body)

    def _getData_cardinality(self, index, time_start, time_end, interval, field):
        aggs = {'some_cardinality': {'cardinality': {'field': field}}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": '*',
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": {
                'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }
                        },
                    "aggs": aggs
                    }
                }
            })
        return self.es.search(index=index, body=body)

    def _getData_count(self, index, query, time_start, time_end, interval):
        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": query,
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": {
                'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }
                        }
                    }
                }
            })
        return self.es.search(index=index, body=body)

    def _getData_some_top(self, index, time_start, time_end, field, size):
        aggs = {'some_top': {'terms': {'field': field, 'size': size, 'order': {'_count': 'desc'}}}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": "*",
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": aggs
            })
        return self.es.search(index=index, body=body)

    def _getData_has_sub_query(self, index, time_start, time_end, interval, field, sub_fields):
        aggs_master = {}
        aggs_master[field] = {'sum': {"field": field}}
        aggs_sub = {'some_sub': {'filters': {'filters': {}},
                "aggs": {'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }                      
                        },
                    "aggs":aggs_master
                    }}}}
        for sub_field in sub_fields:
            aggs_sub['some_sub']['filters']['filters'][sub_field] = {'query': {'query_string': {
                'query': sub_field,
                'analyze_wildcard': True
                }}}
        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": "*",
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": aggs_sub
            })
        return self.es.search(index=index, body=body)

    def _getData_has_sub_sum(self, index, query, time_start, time_end, interval, fields):
        aggs = {}
        for field in fields:
            aggs[field] = {'sum': {"field": field}}

        body = json.dumps({
            "query": {
                "filtered": {
                    "query": {
                        "query_string": {
                            "query": query,
                            "analyze_wildcard": True
                            }
                        },
                    "filter": {
                        "bool": {
                            "must": [
                                {
                                    "range": {
                                        "@timestamp": {
                                            "gte": time_start,
                                            "lte": time_end
                                            }
                                        }
                                    }
                                ],
                            "must_not": []
                            }
                        }
                    }
                },
            "size": 0,
            "aggs": {
                'data_interval': {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": interval,
                        "pre_zone": "+08:00",
                        "pre_zone_adjust_large_interval": True,
                        "min_doc_count": 1,
                        "extended_bounds": {
                            "min": time_start-10,
                            "max": time_end+10
                            }
                        },
                    "aggs": aggs
                    }
                }
            })
        return self.es.search(index=index, body=body)

    def _formatData_gen(self, data, fields):
        results = {}
        for field in fields:
            results[field] = []
        for result in data['aggregations']['data_interval']['buckets']:
            for field in fields:
                results[field].append(self.format_value(result[field]['value']))
        return results
    
    def _formatData_some_per_sum(self, data, name):
        results = {}
        results[name] = [] 
        for result in data['aggregations']['data_interval']['buckets']:
            results[name].append(self.format_value(result['some_per_sum']['value']))
        return results

    def _formatData_some_sum(self, data, name):
        results = {}
        results[name] = self.format_value(data['aggregations']['some_sum']['value'])
        return results

    def _formatData_cardinality(self, data, name):
        results = {}
        results[name] = []
        for result in data['aggregations']['data_interval']['buckets']:
            results[name].append(self.format_value(result['some_cardinality']['value']))
        return results

    def _formatData_count(self, data, name):
        results = {}
        results[name] = []
        for result in data['aggregations']['data_interval']['buckets']:
            results[name].append(self.format_value(result['doc_count']))
        return results

    def _formatData_some_top(self, data):
        results = {}
        columns = []
        values = []
        for result in data['aggregations']['some_top']['buckets']:
            columns.append(result['key'])
            values.append(self.format_value(result['doc_count']))
        results = dict(zip(columns, values))
        return results

    def _formatData_has_sub_query(self, data, field):
        results = {}
        for column in data['aggregations']['some_sub']['buckets']:
            results[column] = []
            for result in data['aggregations']['some_sub']['buckets'][column]['data_interval']['buckets']:
                results[column].append(self.format_value(result[field]['value']))
        return results

    def _formatData_has_sub_sum(self, data, fields):
        results = {}
        for column in fields:
            results[column] = []
        for result in data['aggregations']['data_interval']['buckets']:
            for column in fields:
                results[column].append(self.format_value(result[column]['value']))
        return results

    def getData_byDSL(self, index, **kw):
        return self.es.search(index=index, **kw)

if __name__ == '__main__':
    es = ElastseData()
    index = 'monitor-%s' % time.strftime('%Y.%m.%d',time.localtime(time.time()))
    print es._getData_gen(index=index, query='type:checkload AND iphost:1.74', time_start=int(time.time()*1000)-900000, time_end=int(time.time()*1000), interval='30s', fields=['load1-1', 'load5-1', 'load15-1'])
#    print es._formatData_has_sub_query(es._getData_has_sub_query(index=index, time_start=int(time.time()*1000)-900000, time_end=int(time.time()*1000), interval='30s', field='byte', sub_fields=['backend:haproxy2', 'backend:haproxy3', 'backend:haproxy4', 'backend:haproxy5']), field='byte')
