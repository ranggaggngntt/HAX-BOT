import requests
import argparse
from multiprocessing.dummy import Pool
from datetime import datetime
import re
from colorama import Fore, init
class Dorker(object):

    URL = []
    Domains = 0
    blacklist = [
        'https://en-int.seekweb.com/',
        'http://en-int.seekweb.com/',
        'en-int.seekweb.com',
        'http://www.zapmeta.ws/',
        'www.zapmeta.ws',
        'http://www.izito.ws/',
        'www.izito.ws',
        'http://apps4u.store/',
        'https://apps4u.store/',
        'apps4u.store',
        'https://www.made-in-china.com/',
        'https://www.domain.com/',
        'https://www.zapmeta.ws/',
        'https://www.izito.ws/',
        'http://About.com/',
        'https://About.com/'
    ]

    def __init__(self, thread_count, choice, dork):
        self.thread_count = thread_count
        self.choice = choice
        self.dork = dork
    
    init(convert=True,autoreset=True)

    def BingDorker(self, dorklist):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}
        try:
            pagereq = requests.get(dorklist, headers=headers)
            checktext = pagereq.text
            checktext = checktext.replace("<strong>","")
            checktext = checktext.replace("</strong>","")
            checktext = checktext.replace('<span dir="ltr">','')
            checksites = re.findall('<cite>(.*?)</cite>',checktext)
            for sites in checksites:
                sites = sites.replace("http://","protocol1")
                sites = sites.replace("https://","protocol2")
                sites = sites + "/"
                site = sites[:sites.find("/")+0]
                site = site.replace("protocol1","http://")
                site = site.replace("protocol2","https://")
                if site in self.blacklist:
                    pass
                elif 'bing.com' in site:
                    pass
                elif '<' in site:
                    pass
                else:
                    if "http" in site:
                        print(Fore.LIGHTBLUE_EX, '[+] {}'.format(site))
                        save = open('bing_result.txt', 'a')
                        save.write(site+'\n')
                        save.close()
                        self.Domains += 1
                    else:
                        print(Fore.LIGHTBLUE_EX,'[+] http://{}'.format(site))
                        save = open('bing_result.txt', 'a')
                        save.write('http://'+site+'\n')
                        save.close()
                        self.Domains += 1
    
        except Exception as e:
            print(e)

    def toUrl(self, dorklist, choice):
        siteDomain = [
            'http://www.bing.com/search?q={}&count=50&first=1',
            'http://www.bing.com/search?q={}&count=50&first=51',
            'http://www.bing.com/search?q={}&count=50&first=101',
            'http://www.bing.com/search?q={}&count=50&first=151',
            'http://www.bing.com/search?q={}&count=50&first=201',
            'http://www.bing.com/search?q={}&count=50&first=251',
            'http://www.bing.com/search?q={}&count=50&first=351',
            'http://www.bing.com/search?q={}&count=50&first=401',
        ]
        siteIp = [
            'http://www.bing.com/search?q=ip:{}&count=50&first=1',
            'http://www.bing.com/search?q=ip:{}&count=50&first=51',
            'http://www.bing.com/search?q=ip:{}&count=50&first=101',
            'http://www.bing.com/search?q=ip:{}&count=50&first=151',
            'http://www.bing.com/search?q=ip:{}&count=50&first=201',
            'http://www.bing.com/search?q=ip:{}&count=50&first=251',
            'http://www.bing.com/search?q=ip:{}&count=50&first=351',
            'http://www.bing.com/search?q=ip:{}&count=50&first=401',
        ]
        if choice == '1':
            for i in dorklist:
                for page in siteDomain:
                    dork = page.format(i)
                    self.URL.append(dork)
        else:
            for i in dorklist:
                for page in siteIp:
                    dork = page.format(i)
                    self.URL.append(dork)

    def run(self):
        self.toUrl(self.dork, self.choice)
        with Pool(self.thread_count) as worker:
            worker.map(self.BingDorker, self.URL)
            worker.close()
            worker.join()
        return print('Saved As bing_result.txt')
