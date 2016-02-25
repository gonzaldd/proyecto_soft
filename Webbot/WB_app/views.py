from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from urllib2 import *
import urllib


def get_id(request,id_solicitud):
    print id_solicitud

    conn = urlopen('http://localhost:8983/solr/Index/select?q=id:'+id_solicitud+'&wt=json')
    rsp = eval( conn.read() )

    print "number of matches=", rsp['response']['numFound']
    return JsonResponse(rsp['response'])

def get_list(request):
    conn = urlopen('http://localhost:8983/solr/Index/select?q=*:*&wt=json&rows=10000')
    rsp = eval( conn.read() )
    return JsonResponse(rsp['response'])

def get_autor(request,nombre):
    print nombre
    
    url = 'http://localhost:8983/solr/Index/select?q=Autor:"'+urllib.quote(nombre)+'"&wt=json&rows=10000'
    conn = urlopen(url)
    rsp = eval( conn.read() )

    return JsonResponse(rsp['response'])

def get_titulo(request,titulo):
    print titulo
    
    url = 'http://localhost:8983/solr/Index/select?q=Titulo:"'+urllib.quote(titulo)+'"&wt=json&rows=10000'
    conn = urlopen(url)
    rsp = eval( conn.read() )

    return JsonResponse(rsp['response'])

def get_url(request,uu):
    print uu
    
    url = 'http://localhost:8983/solr/Index/select?q=URL:"'+urllib.quote(uu)+'"&wt=json&rows=10000'
    conn = urlopen(url)
    rsp = eval( conn.read() )

    return JsonResponse(rsp['response'])

def get_isbn(request,isbn):
    print isbn
    
    url = 'http://localhost:8983/solr/Index/select?q=ISBN:"'+urllib.quote(isbn)+'"&wt=json&rows=10000'
    conn = urlopen(url)
    rsp = eval( conn.read() )

    return JsonResponse(rsp['response'])

def get_anio(request,anio):
    print anio
    
    url = 'http://localhost:8983/solr/Index/select?q=Anio:"'+urllib.quote(anio)+'"&wt=json&rows=10000'
    conn = urlopen(url)
    rsp = eval( conn.read() )

    return JsonResponse(rsp['response'])