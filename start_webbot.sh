#!/bin/bash

SCRIPTPATH=$(pwd)
cd ${SCRIPTPATH}/proyecto_soft/scrapy_crawler

PATH=$PATH:/usr/local/bin
export PATH

wget 'http://localhost:8983/solr/Index/update?stream.body=<delete><query>*:*</query></delete>&commit=true'

scrapy crawl crawler

wait

wget http://localhost:8983/solr/Index/dataimport?command=full-import
