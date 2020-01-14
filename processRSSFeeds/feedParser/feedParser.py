from bs4 import BeautifulSoup

class FeedParser():
    def __init__(self, outputFile):
        handler = open(outputFile).read()
        self.soup = BeautifulSoup(handler, 'lxml')

    def getItems(self, n):
        i = 1
        # get last n items
        myString = ""
        for message in self.soup.findAll('item'):
            myString += str(message)
            if i is n:
                break
            i = i + 1
        return(myString)
