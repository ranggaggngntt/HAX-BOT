import proxygrab
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
import requests
from multiprocessing.dummy import Pool

class Checker(object):

    def __init__(self, thread_count, proxy):
        self.thread_count = thread_count
        self.proxy = proxy

    def check(self, proxyList):
        try:
            http_proxy = 'http://'+proxyList
            https_proxy = 'https://'+proxyList
            proxyDict = {
                'http': http_proxy,
                'https': https_proxy
            }
            req = requests.get('http://api.hackertarget.com/reverseiplookup/?q=8.8.8.8', proxies=proxyDict, timeout=15)
            if req:
                if 'API count exceeded' in req.text:
                    pass
                else:
                    save = open('proxy.txt','a')
                    save.write(proxyList+'\n')
                    save.close()
            else:
                pass
        except Exception:
            pass
        
    def run(self):
        with Pool(self.thread_count) as worker:
            worker.map(self.check, self.proxy)
            worker.close()
            worker.join()

def create_proxy():
    proxy = []
    print('Scrape Proxy')
    try:
        print('Scrape From Proxy_List_Scrapper')
        SSL = 'https://www.sslproxies.org/',
        GOOGLE = 'https://www.google-proxy.net/',
        ANANY = 'https://free-proxy-list.net/anonymous-proxy.html',
        UK = 'https://free-proxy-list.net/uk-proxy.html',
        US = 'https://www.us-proxy.org/',
        NEW = 'https://free-proxy-list.net/',
        SPYS_ME = 'http://spys.me/proxy.txt',
        PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
        PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
        PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
        PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
        PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
        PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'
        ALL = 'ALL'
        scrapper = Scrapper(category=ALL, print_err_trace=False)
        data = scrapper.getProxies()

        for item in data.proxies:
            proxy.append('{}:{}'.format(item.ip, item.port))
    except:
        pass
    try:
        print('Scrape Socks4 Proxy')
        socks4 = proxygrab.get_socks4(method='all')
        proxy.extend(socks4)
    except:
        pass
    try:
        print('Scrape Socks5 Proxy')
        socks5 = proxygrab.get_socks5(method='all')
        proxy.extend(socks5)
    except:
        pass
    try:
        print('Scrape http Proxy')
        http = proxygrab.get_http(method='all')
        proxy.extend(http)
    except:
        pass
    try:
        print('Scrape https Proxy')
        https = proxygrab.get_https(method='all')
        proxy.extend(https)
    except:
        pass
    
    #Thread Default 100 tinggal ganti doang
    check = Checker(100, proxy)
    check.run()

    return print('Done')