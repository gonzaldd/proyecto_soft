#!/bin/bash

SCRIPTPATH=$(pwd)
cd ${SCRIPTPATH}/proyecto_soft/scrapy_crawler

PATH=$PATH:/usr/local/bin
export PATH

scrapy crawl crawler

wait

wget http://localhost:8983/solr/Index/dataimport?command=full-import
