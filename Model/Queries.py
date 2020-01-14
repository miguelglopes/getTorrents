from peewee import IntegrityError
from Model.Show import Episode

   
def getAllNotDownloadedEpisodes():
    return list(Episode.select().where(Episode.downloaded==False))

def updateDownloadedState(self, traktid, downloadedState):
    sql = "UPDATE `latestEpisode` SET `downloaded`=%s WHERE `traktid`=%s"
    self._connection.cursor().execute(sql, (downloadedState, traktid))
    self._connection.commit()

def updateListDownloadedState(self, torrentList):
    for i in torrentList:
        self.updateDownloadedState(i.traktId, 1)

def insertShowsList(showList):
    for s in showList:
        try:
            s.save(force_insert=True)
        except IntegrityError: #alreadyInserted
            continue

def insertEpisodesList(episodesList):
    for e in episodesList:
        try:
            e.save(force_insert=True)
        except IntegrityError: #alreadyInserted
            continue