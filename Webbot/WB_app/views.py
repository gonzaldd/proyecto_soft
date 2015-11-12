from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from urllib2 import *

def get_id(request,id_solicitud):
    print id_solicitud

    conn = urlopen('http://localhost:8983/solr/Index/select?q=id:'+id_solicitud+'&wt=json')
    rsp = eval( conn.read() )

    print "number of matches=", rsp['response']['numFound']
    return JsonResponse(rsp)

def get_list(request):
    conn = urlopen('http://localhost:8983/solr/Index/select?q=*:*&wt=json')
    rsp = eval( conn.read() )
    return JsonResponse(rsp)

def get_autor(request,nombre):
    print nombre

    conn = urlopen('http://localhost:8983/solr/Index/select?q=Autor:"'+nombre+'"&wt=json')
    rsp = eval( conn.read() )
    return JsonResponse(rsp)