'''
Created on 21/09/2017

@author: migue
'''

import datetime
from processRSSFeeds.feedParser.feedParser import FeedParser
from config.Config import Config

class FeedGenerator(Config):
    
    def __init__(self, torrentList):
        super().__init__()
        self._maxFeedItems = int(self.config.get("RssFeed", "maxFeedItems"))
        self._rssTitle = self.config.get("RssFeed", "rssTitle")
        self._rssDescription = "migasll torrent feed"
        self._rssSiteURL = "http://rss.migasll.club/"
        self._rssLink = self._rssSiteURL + "/index.html"
        self.torrentsList = torrentList

    def createRssFeed(self):
        if(len(self.torrentsList) > 0):
            self._torrentList = self.torrentsList
            self._outputFileName = self.config.get("RssFeed", "outputFile")
            self._torrentCount = len(self.torrentsList)
            self._restOfFile = FeedParser(self._outputFileName).getItems(self._maxFeedItems - self._torrentCount)
            self._outputFile = open(self._outputFileName, "w")
            self._now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
    
            self._writeHeader()
            self._writeItems()
            self._writeFooter()

    def _writeHeader(self):
        self._outputFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
        self._outputFile.write("<rss version=\"2.0\" xmlns:torrent=\"" + self._rssSiteURL + "\">\n")
        self._outputFile.write("<channel>\n")
        self._outputFile.write("<title>" + self._rssTitle + "</title>\n")
        self._outputFile.write("<link>" + self._rssLink + "</link>\n")
        self._outputFile.write("<description>" + self._rssDescription + "</description>\n")
        self._outputFile.write("<lastBuildDate>" + self._now + "</lastBuildDate>\n")

    def _writeItems(self):
        for torrent in self._torrentList:
            self._outputFile.write("<item>\n")
            self._outputFile.write("<title>" + torrent.name + "</title>\n")
            self._outputFile.write("<category>" + torrent.category + "</category>\n")
            self._outputFile.write("<link>" + torrent.magnet + "</link>\n")
            self._outputFile.write("<guid isPermaLink=\"false\">" + torrent.magnet + "</guid>\n")
            self._outputFile.write("<description> &lt;a href=\"" + self._now + "\"&gt;MAGNET:" + torrent.name + "&lt;/a&gt;</description>\n")
            self._outputFile.write("<pubDate>" + self._now + "</pubDate>\n")
            self._outputFile.write("</item>\n")
        self._outputFile.write(self._restOfFile)
    
    def _writeFooter(self):
        self._outputFile.write("</channel>\n")
        self._outputFile.write("</rss>")
        self._outputFile.close()
