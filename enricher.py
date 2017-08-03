#!/usr/bin/python
# -*- coding: utf-8 -*-

from FMStats import fetcher
import json
import urllib2

class LastFMenricher(fetcher.FmFetcher):
    """
    LastFM API credentials
    """
    lastFMbaseUrl = "http://ws.audioscrobbler.com/2.0/"
    apiKey = "0e3e23795845a7af026e066f0e1e62ae"
    outputFormat = "json"

    """
    Builds up an API url for Artist info
    """
    def lastFmArtist(self):
        method = "?method=artist.getinfo"
        apiUrl = "%s%s&api_key=%s&format=%s&artist=" % (self.lastFMbaseUrl, method, self.apiKey, self.outputFormat)
        return apiUrl

    """
    Takes a serialized string, decodes it and builds LastFM API URL for
    the artist info
    """
    def urlBuilder(self, fmEntry):
        artistUrl = self.lastFmArtist()
        decoded = json.loads(fmEntry)
        artistName = urllib2.quote(decoded['artist'].encode('utf-8'))
        url = "%s%s" % (artistUrl, artistName)
        return url
    """
    Takes response from LastFM API, collects only interesting stuff from returned
    JSON and builds up enriched JSON which is later used.
    """
    def dataEnricher(self, fmUrl):
        response = urllib2.urlopen(fmUrl)
        response = response.read()
        decode = json.loads(response)
        lastFm = {}
        lastFm['url'] = decode['artist']['url']
        lastFm['image'] = decode['artist']['image'][3]['#text']
        lastFm['name'] = decode['artist']['name']
        lastFm['country'] = None

        genre = []
        # Iterates over tags and adds them in a single genre list.
        for tag in decode['artist']['tags']['tag']:
            genre.append(tag['name'])

        lastFm['genre'] = genre
        lastFm = json.dumps(lastFm, ensure_ascii=False).encode('utf8')
        return lastFm
