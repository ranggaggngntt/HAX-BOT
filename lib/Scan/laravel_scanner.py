import requests
from multiprocessing import Pool
from colorama import Fore, init
class LaravelScanner(object):

    def __init__(self, site, thread):
        self.site = site
        self.thread = thread
    init(convert=True, autoreset=True)
    def Scan(self, site):
        try:
            laravelCookie = requests.get(site, timeout=10, verify=False, allow_redirects=False)
            if 'laravel_session' in laravelCookie.cookies:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found Laravel Cookie'.format(site))
                save = open('laravel.txt', 'a')
                save.write(site+'\n')
                save.close()
            else:
                print(Fore.LIGHTRED_EX, '[+] {} : Not Found'.format(site))
                save = open('unknown_cms.txt', 'a')
                save.write(site+'\n')
                save.close()
        except Exception:
            pass
    
    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.Scan, self.site)
            worker.close()
            worker.join()
        return print('Saved As laravel.txt')