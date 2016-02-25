#!/bin/bash


clear
SCRIPTPATH=`pwd -P`
cd ${SCRIPTPATH}/scrapy
scrapy crawl crawler
echo 'PAGINAS CARGADAS'
cd ..
cd ${SCRIPTPATH}/Webbot
./start.sh
echo 'SERVIDOR ACTIVADO'
$SHELL
