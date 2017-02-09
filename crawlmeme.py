import requests
from bs4 import BeautifulSoup
import wget

def getDank():
    imgbase = 'https://imgflip.com/s'
    imgend = '.jpg'
    base = 'https://imgflip.com/memetemplates?page='

    pagestart = 1
    pageLimit = 22

    for i in range(pagestart,pageLimit):
        session = requests.session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
        })
        session = session.get(base+str(i))
        homepage = session.text
        soup = BeautifulSoup(homepage)
        for comment in soup.findAll('h3',{'class':'mt-title'}):
            print comment
            for a in comment.findAll('a', href=True):
                ahref = a.get('href')
                print ahref
                filename = wget.download(imgbase+ahref+imgend, 'yourdirectory')





