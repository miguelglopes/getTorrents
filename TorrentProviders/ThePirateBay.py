from config.exceptions.NoHTMLException import NoHTMLException
from config.exceptions.NoResultsFound import NoResultsFound
from config.exceptions.ParseHTMLException import ParseHTMLException
from TorrentProviders.GeneralTorrentProvider import GeneralTorrentProvider
from TorrentProviders.Torrent import _Torrent
from config import Common

class ThePirateBay(GeneralTorrentProvider):
    def __init__(self):
        super().__init__("The Pirate Bay")

    def _get_html(self):
        try:
            search = "/search/%s/" % (self.title)
            self.soup = Common.getUrlSoup(self.proxy + search)
            print("fetching")
            print("fetched")
        except Exception as e:
            print(e)
            raise NoHTMLException(e)

    def _parse_html(self):
        try:
            content = self.soup.find('table', id="searchResult")
            
            if content is None:
                message = "No results found for given input!"
                print(message)
                raise NoResultsFound(message)
                
            self.showTorrentList = list()
            
            data = content.find_all('tr')
            for i in data[1:]:
                
                torrent = _Torrent()
                
                torrent.name = i.find('a', class_='detLink').string
                torrent.uploader = i.find('font', class_="detDesc").a
                if torrent.name is None:
                    torrent.name = i.find('a', class_='detLink')['title'].split(" ")[2:]
                    torrent.name = " ".join(str(x) for x in torrent.name)
                if torrent.uploader is None:
                    torrent.uploader = i.find('font', class_="detDesc").i.string
                else:
                    torrent.uploader = torrent.uploader.string
                if self.OS_WIN:
                    torrent.name = torrent.name.encode('ascii', 'replace').decode()
                comments = i.find(
                    'img', {'src': '//%s/static/img/icon_comment.gif' % (self.proxy.split('/')[2])})
                if comments is None:
                    torrent.comment = '0'
                else:
                    torrent.comment = comments['alt'].split(" ")[-2]
                is_vip = i.find('img', {'title': "VIP"})
                is_trusted = i.find('img', {'title': 'Trusted'})
                if(is_vip is not None):
                    torrent.isVIP = True
                elif(is_trusted is not None):
                    torrent.isTrusted = True
                torrent.category = i.find('td', class_="vertTh").find_all('a')[0].string
                torrent.subCategory = i.find('td', class_="vertTh").find_all('a')[1].string
                torrent.seeds = int(i.find_all('td', align="right")[0].string.strip())
                torrent.leeches = int(i.find_all('td', align="right")[1].string.strip())
                torrent.date = i.find('font', class_="detDesc").get_text().split(' ')[1].replace(',', "")
                torrent.size = Common.getSize(i.find('font', class_="detDesc").get_text().split(' ')[3].replace(',', ""))
                torrent.torrentID = i.find('a', {'class': 'detLink'})["href"].split('/')[2]
                torrent.link = "%s/torrent/%s" % (self.proxy, torrent.torrentID)
                torrent.magnet = (i.find_all('a', {'title': 'Download this torrent using magnet'})[0]['href']).replace("&", "&amp;")
                
                self._addTorrent(torrent)
                    
            print("Results fetched successfully!")
        except Exception as e:
            print(e)
            raise ParseHTMLException(e)

    
    def getEpisodes(self, episodesList):
        torrentsList = []
        for episode in episodesList:
            searchString = episode.show.title + " S" + format(episode.season, '02') + "E" + format(episode.episode, '02')
            selectedTorrent = self.getTorrents(searchString).selectedTorrent
            if (selectedTorrent is not None):
                selectedTorrent.traktId=episode.show.traktid
                torrentsList.append(selectedTorrent)
        return torrentsList
