#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConfigParser as cp

class ConfManager(object):

    def __init__(self):
        self.config = cp.ConfigParser()
        self.config.read(["./config/fmstats.ini", "./FMStats/config/fmstats.ini"])


    def playlistUrl(self):
        playlist = self.config.get("Base","playlist_url")
        return playlist

    def elasticAddres(self):
        elastic = {}
        elastic['host'] = self.config.get("ElasticSearch", "hostname")
        elastic['port'] = self.config.get("ElasticSearch", "http_port")
        return elastic

    def artistIndex(self):
        return self.config.get("ElasticSearch", "artist_index")

    def artistMapping(self):
        return self.config.get("ElasticSearch", "lastfmEsMapping")

    def radioIndex(self):
        return self.config.get("ElasticSearch", "radio_index")

    def radioMapping(self):
        return self.config.get("ElasticSearch", "radiofmEsMapping")
