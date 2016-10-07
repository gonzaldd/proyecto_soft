#!/bin/bash

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
cd ${SCRIPTPATH}/scrapy_crawler

PATH=$PATH:/usr/local/bin
export PATH

wget 'http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/update?stream.body=<delete><query>*:*</query></delete>&commit=true'

scrapy crawl crawler

wait

wget http://laboratorio3.sistemas.unla.edu.ar:8983/solr/Index/dataimport?command=full-import
