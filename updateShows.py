from ListProviders.Trakt import Trakt
from Model import Queries

t = Trakt()

#get shows and save    
sl = t.getShowList("migasll", "plexSeries")
Queries.insertShowsList(sl)

#get episodes and save
el = t.getShowsEpisodes(sl)
Queries.insertEpisodesList(el)