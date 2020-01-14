from Model import Queries
from TorrentProviders.ThePirateBay import ThePirateBay

t = ThePirateBay()

#get torrents and generate feed
allEpisodes = Queries.getAllNotDownloadedEpisodes()
torrentList = t.getEpisodes(allEpisodes)
#mc.updateListDownloadedState(torrentList)
#FeedGenerator(torrentList).createRssFeed()

print("ola")