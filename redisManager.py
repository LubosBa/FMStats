#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis

redInstance = redis.StrictRedis(host="172.17.0.8", port=6379, db=0)

def redisPublishArtists(artistList):
    redInstance.ltrim("fmList", "-1", "0")
    for artist in artistList:
        redInstance.lpush("fmList", artist)

def redisReadArtists():
    lenght = redInstance.llen("fmList")
    size = 0
    artists = []
    while size < lenght:
        artist = redInstance.lindex("fmList", size)
        size += 1
        artists.append(artist)
    return artists
