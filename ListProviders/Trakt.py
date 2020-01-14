from config import Common
import json
from Model.Show import Show, Episode

class Trakt():

    def __init__(self):
        super().__init__()
        self.baseUrl = "https://api.trakt.tv"
        self.apiKey = Common.config["trakt"]["apiKey"]
    
    def _getRequest(self, url):
        headers = {'Content-Type':'application/json', 'trakt-api-version':'2', 'trakt-api-key':self.apiKey}
        reponse = Common.http_request(url, headers)
        return(reponse)

    def getShowEpisodes(self, show):
        url = self.baseUrl + "/shows/" + str(show.traktid) + "/seasons?extended=full"
        rawEpisodes = self._getRequest(url)
        return self._processRawEpisodes(rawEpisodes, show)

    def getShowsEpisodes(self, shows):
        episodesList = []
        for show in shows:
            episodesList.extend(self.getShowEpisodes(show))
        return episodesList
    
    def getNextEpisode(self, show):
        url = self.baseUrl + "/shows/" + str(show.traktid) + "/last_episode"
        return self._getRequest(url)

    def getShowList(self, user, listID):
        mediaType="show"
        url = self.baseUrl + "/users/" + user + "/lists/" + listID + "/items/" + mediaType
        rawList = self._getRequest(url)
        return self._processRawList(rawList)

    def _processRawList(self, rawList):
        j = json.loads(rawList)
        showList = []
        for item in j:
            show = Show()
            show.title = item["show"]["title"]
            show.year = int(item["show"]["year"])
            show.traktid = int(item["show"]["ids"]["trakt"])
            show.tvdbid = int(item["show"]["ids"]["tvdb"])
            show.imdbid = item["show"]["ids"]["imdb"]
            show.tmdbid = int(item["show"]["ids"]["tmdb"])
            show.tvrageid = item["show"]["ids"]["tvrage"]
            showList.append(show) 
        return showList         

    def _processRawEpisodes(self, rawEpisodes, show):
        j = json.loads(rawEpisodes)
        episodesList = []
        for season in j:
            seasonNum = season["number"]
            if Common.toInt(seasonNum)>0:
                for i in range(1, season["episode_count"]+1):
                    episode = Episode()
                    episode.show = show
                    episode.season = seasonNum
                    episode.episode = i
                    episode.downloaded = False
                    episodesList.append(episode)
        return episodesList 