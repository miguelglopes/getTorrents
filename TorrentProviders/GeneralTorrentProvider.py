'''
Created on 10/10/2017

@author: migue
'''
from config.exceptions.NoProxyAvailableException import NoProxyAvailableException
from config.exceptions.NoResultsFound import NoResultsFound
from config import Common
from guessit import guessit
from config.Common import config


class GeneralTorrentProvider():
    def __init__(self, torrentName):
        self.TorrentName = torrentName
        self.proxies = config["torrents"]["tbpProxies"]
        self.proxy = self._check_proxy() #TODO IS THIS WORKING???
        self.soup = None
        self.showTorrentList = None
        self.selectedTorrent = None
        self.OS_WIN = True
        
    def getTorrents(self, title):
        self.title = Common.cleanString(title)
        self._get_html()
        try:
            self._parse_html()
        except (NoResultsFound):
            self.selectedTorrent = None
        self._select_torrent()
        return self

    def _check_proxy(self):
        count = 0
        for proxy in self.proxies:
            print("Trying %s" % proxy)
            try:
                self.soup = Common.getUrlSoup(proxy)
                count += 1
                if self.soup == -1 or self.soup.a.string != self.TorrentName:
                    print("Bad proxy!")
                    if count == len(self.proxies):
                        message = "No proxies available found!"
                        raise NoProxyAvailableException(message)
                    else:
                        continue
                else:
                    return(proxy)
            except NoProxyAvailableException as e:
                print(e)
            except Exception as e:
                print(e)
                continue
           
    def _select_torrent(self):
        
        minSeeds = int(config["torrents"]["minSeeds"])
        maxLeeches = int(config["torrents"]["maxLeeches"])
        maxSize = int(config["torrents"]["maxSize"])
        minSize = int(config["torrents"]["minSize"])
        screenSize = list(config["torrents"]["screenSize"])
        categories = list(config["torrents"]["categories"])
        subCategories = list(config["torrents"]["subCategories"])
        
        if self.showTorrentList is not None:
            for t in self.showTorrentList:
                if t.isTrusted or t.isVIP:
                    self.selectedTorrent = t
                    if any(item == t.category for item in categories) and any(item == t.subCategory for item in subCategories):
                        self.selectedTorrent = t
                        if t.seeds >= minSeeds and t.leeches <= maxLeeches:
                            self.selectedTorrent = t
                            if t.size <= maxSize and t.size >= minSize:
                                self.selectedTorrent = t
                                if any(item == t.screenSize for item in screenSize):
                                    self.selectedTorrent = t
                                    break
    
    def _addTorrent(self, torrent):
        dic = guessit(torrent.name)
        if(torrent.season is None):
            torrent.season = Common.getKey(dic, "season")
        if(torrent.episode is None):
            torrent.episode = Common.getKey(dic, "episode")
        if(torrent.screenSize is None):
            torrent.screenSize = Common.getKey(dic, "screen_size")
        if(torrent.videoCodec is None):
            torrent.videoCodec = Common.getKey(dic, "video_codec")
        if(torrent.audioCodec is None):
            torrent.audioCodec = Common.getKey(dic, "audio_codec")
        if(torrent.format is None):
            torrent.format = Common.getKey(dic, "format")

        self.showTorrentList.append(torrent)
