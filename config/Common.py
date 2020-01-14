import re
from bs4 import BeautifulSoup
from config.exceptions.HttpRequestException import HttpRequestException
import requests
import logging
import os
import json

config=None
full_config_dir = "C:\\Miguel\\Nextcloud\\projetos\\rssFeeds\\"
config_file_name = "config.json"
config_file = os.path.join(full_config_dir, config_file_name)
logger = logging.getLogger('log1')

with open(config_file) as config_file:
    config = json.load(config_file)

def http_request(url, headersDic=None, timeout=15):
    try:
        return requests.get(url, headers=headersDic, timeout=timeout).content
    except Exception as e:
        raise HttpRequestException(e)
        
def getUrlSoup(url):
    try:
        raw = http_request(url)
        soup = BeautifulSoup(raw, 'lxml')
        return soup
    except Exception as e:
        raise HttpRequestException(e)
    

def getSize(stringSize):
    """
    All sizes need to be converted to mebibytes (MiB)
    """
    if "MiB" in stringSize:
        return float(stringSize.replace("MiB", "").strip())
    elif "GiB" in stringSize:
        return float(stringSize.replace("GiB", "").strip()) * 1024
    elif "KiB" in stringSize:
        return float(stringSize.replace("KiB", "").strip()) / 1024
    elif "B" in stringSize:
        return float(stringSize.replace("B", "").strip()) / (2 ** 20)
    else:
        print(stringSize + "ERROR ON SIZE!!")

def cleanString(stringToClean):
    return re.sub('[^a-zA-Z0-9!:.?,& -]', '', stringToClean)

def getKey(dic, key):
    try:
        return dic[key]
    except KeyError:
        return None

def toInt(s, defaultValue=0):
    try: 
        return int(s)
    except ValueError:
        return defaultValue