from gettext import install
import sys
import wget
import requests
import dload
from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Get OS for Chrome driver download
def getDriverOS():
    validOS = ''
    # Valid OS names for downloading Chrome driver 
    validPlatforms = {
        'linux1' : 'linux64',
        'linux2' : 'linux64',
        'darwin' : 'mac64',
        'win32' : 'win32'
    }
    try:
        validOS = validPlatforms[sys.platform]
    except:
        print('OS is not support by Chrome driver')
    finally:
        return(validOS)

# Downlaod Stable Chrome driver exe
def getStableV():
    req  = requests.get('https://chromedriver.chromium.org/home')
    soup = BeautifulSoup(req.text, "html.parser")
    strLink = [] ; latestAndStable = []
    # find stable release link(a) href attribute 
    for a in soup.find_all('a'):
        if type(a.get('href')) == str:
            strLink.append(a.get('href'))
    for l in strLink:
        if 'https://chromedriver.storage.googleapis.com/index.html?' in l:
            latestAndStable.append(l)
    # return zip downlaod link of stable
    zipDriver = latestAndStable[1].replace('index.html?path=', '') + 'chromedriver_' + getDriverOS() + '.zip'
    return(zipDriver)

parentDirOfDriver = print(dload.save_unzip(getStableV()))
