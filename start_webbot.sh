#!/bin/bash

SCRIPTPATH=$(pwd)
cd ${SCRIPTPATH}/scrapy_crawler

PATH=$PATH:/usr/local/bin
export PATH

scrapy crawl crawler

wget http://localhost:8983/solr/Index/dataimport?command=full-import
