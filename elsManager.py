#!/usr/bin/python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch, client
from FMStats import confManager as cm
import json

# Configuration
conf = cm.ConfManager()
es = Elasticsearch([conf.elasticAddres()])
ec = client.IndicesClient(es)


def checkIndex(esIndex):
    if ec.exists(index=esIndex):
        return True
    else:
        return False

def createIndex(esIndex, esMapping):
    mapping = open(esMapping, 'r')
    mapping = mapping.read()
    ec.create(index=esIndex, body=mapping)

def mappingInit():
    if checkIndex(conf.artistIndex()) == False:
        createIndex(conf.artistIndex(), conf.artistMapping())
    if checkIndex(conf.radioIndex()) == False:
        createIndex(conf.radioIndex(), conf.radioMapping())
    return True # All indices inicialized.
