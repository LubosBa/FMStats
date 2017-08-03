#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import json
import datetime, time

class FmFetcher(object):
    url = 0
    """
    Fetches playlist from Radio FM website
    """
    def __init__(self, url):
        self.url = url

    """
    Returns HTML page containing playlist
    """
    def getPlaylist(self):
        response = urllib2.urlopen(self.url)
        return response.read()

    """
    Pulls the table containing songs from html
    """
    def displayPlayHistory(self):
        webpage = self.getPlaylist()
        playlist = []
        bs = BeautifulSoup(webpage, 'html.parser', from_encoding="utf-8")
        table = bs.tbody.find_all('tr')
        # Iterates over found table rows and returns only tds
        for entry in table:
            entry = entry.find_all('td')
            playlist.append(entry)
        return playlist

    """
    Rebuils given list of songs into a nicer format by removing tds.
    Returns 2 dimensional list of radio stats.
    """
    def listFormater(self):
        parsed = []
        # Iterates over 2 dimensional list to clean it up.
        for entry in self.displayPlayHistory():
            rebuild = []
            # Create a list out of td values
            for string in entry:
                rebuild.append(string.string)
            parsed.append(rebuild)
        return parsed

    """
    Returns a list containing json objects of all fetched plays from the Radio
    playlist
    """
    def jsonBuilder(self):
        json_list = []
        for entryList in self.listFormater():
            stats = {}
            date = entryList[0] + " " + entryList[1]
            stats['playDate'] = self.dateConvert(date)
            stats['artist'] = entryList[2]
            stats['song'] = entryList[3]
            json_list.append(json.dumps(stats, ensure_ascii=False).encode('utf8'))
        return json_list

    """
    Converts date into epoch seconds and UTC.
    """
    def dateConvert(self, date):
        epoch = time.mktime(datetime.datetime.strptime(date, "%d.%m.%Y %H:%M").timetuple())
        return int(epoch)



if __name__ == "__main__":
    # execute only if run as a script
    print "Can not run standalone this is a module."
