import requests
from multiprocessing import Pool
from colorama import Fore, init
class ReverseIP(object):

    def __init__(self, thread, ip, proxy):
        self.thread = thread
        self.ip = ip
        self.proxy = proxy

    init(convert=True,autoreset=True)

    def reverse(self, ip):
        try:
            http_proxy = 'http://'+self.proxy
            https_proxy = 'https://'+self.proxy
            proxyDict = {
                'http': http_proxy,
                'https': https_proxy
            }
            api = 'http://api.hackertarget.com/reverseiplookup/?q='+ip
            request = requests.get(api, proxies=proxyDict, timeout=10)
            if request:
                if 'error' in request.text or 'No DNS' in request.text:
                    pass
                elif 'API count exceeded' in request.text or 'Bad Request' in request.text:
                    pass
                elif '<' in request.text or '>' in request.text:
                    pass
                else:
                    print(Fore.LIGHTGREEN_EX ,'Reversing IP: {}\n'.format(ip))
                    print(Fore.LIGHTBLUE_EX ,'=> {}'.format(request.text))
                    open('reversed.txt','a').write(request.text+'\n')
                    pass
        except Exception as e:
            open('err_ip.txt','a').write(ip+'\n')

    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.reverse, self.ip)
            worker.close()
            worker.join()
        return print('Saved As reversed.txt')