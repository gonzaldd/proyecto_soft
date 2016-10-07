from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from urllib2 import *
import urllib
import requests


def get_id(request,id_solicitud):
    print id_solicitud
    try:
        conn = urlopen('http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=id:'+id_solicitud+'&wt=json')
        rsp = eval( conn.read() )

        print "number of matches=", rsp['response']['numFound']
        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por id.'})

def get_list(request):
    try:
        conn = urlopen('http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=*:*&wt=json&rows=10000')
        rsp = eval( conn.read() )
        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer todo.'})

def get_autor(request,nombre):
    print nombre
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Autor:('+urllib.quote(nombre)+')&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por autor.'})

def get_titulo(request,titulo):
    print titulo
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Titulo:('+urllib.quote(titulo)+')&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por titulo.'})

def get_url(request,uu):
    print uu
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=URL:"'+urllib.quote(uu)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por url.'})

def get_isbn(request,isbn):
    print isbn
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=ISBN:"'+urllib.quote(isbn)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por isbn.'})

def get_anio(request,anio):
    print anio
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/select?q=Anio:"'+urllib.quote(anio)+'"&wt=json&rows=10000'
        conn = urlopen(url)
        rsp = eval( conn.read() )

        return JsonResponse(rsp['response'])
    except:
        return JsonResponse({'Estado : ':'Error al traer por anio.'})

def get_indexar(request):
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/dataimport?command=full-import'
        result = requests.get(url)
        if(result.status_code == 200):
            return JsonResponse({'Estado : ':'Indexado OK.'})
    except:
        return JsonResponse({'Estado': 'Error en el indexado.'})

def get_desindexar(request):
    try:
        url = 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/update?stream.body=<delete><query>*:*</query></delete>&commit=true'
        result = requests.get(url)
        if(result.status_code == 200):
            return JsonResponse({'Estado : ':'Desindexado OK.'})
    except:
        return JsonResponse({'Estado : ':'Error en el desindexado.'})