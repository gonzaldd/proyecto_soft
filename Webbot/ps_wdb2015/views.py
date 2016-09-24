from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from urllib2 import *
import urllib


def get_id(request,id_solicitud):
    print id_solicitud
    try:
        conn = urlopen('http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=id:'+id_solicitud+'&wt=json')
        rsp = eval( conn.read() )

        print "number of matches=", rsp['response']['numFound']
        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_list(request):
    try:
        conn = urlopen('http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=*:*&wt=json&rows=10000')
        rsp = eval( conn.read() )
        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_autor(request,nombre):
    print nombre
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Autor:('+urllib.quote(nombre)+')&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_titulo(request,titulo):
    print titulo
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Titulo:('+urllib.quote(titulo)+')&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_url(request,uu):
    print uu
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=URL:"'+urllib.quote(uu)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_isbn(request,isbn):
    print isbn
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=ISBN:"'+urllib.quote(isbn)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})

def get_anio(request,anio):
    print anio
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Anio:"'+urllib.quote(anio)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({})
