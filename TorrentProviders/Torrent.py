'''
Created on 19/09/2017

@author: migue
'''
import logging

class _Torrent():
    
    def __init__(self):

        self.uploader = None
        self.seeds = 0
        self.leeches = 0
        self.date = False
        self.comment = 0
        self.magnet = None
        self.link = None
        self.isVIP = False
        self.isTrusted = False
        self.torrentID = None
        
        self.size = 0
        self.category = None
        self.subCategory = None
        self.name = None
        
        self.season = 0
        self.episode = 0
        self.screenSize = None
        self.videoCodec = None
        self.audioCodec = None
        self.format = None
        
        self.traktId = None
    
    def __str__(self):
        return(str(self.category) + "| " + str(self.subCategory) + "| " + str(self.name) + "| " + str(self.size) + "| "
               + str(self.magnet) + "| " + str(self.link) + "| " + str(self.isVIP) + "| " + str(self.isTrusted) + "| "
               + str(self.season) + "| " + str(self.episode) + "| " + str(self.screenSize) + "| " + str(self.format) + "| "
               + str(self.seeds) + "| " + str(self.leeches))

