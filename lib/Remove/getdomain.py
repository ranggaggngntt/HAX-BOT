from datetime import datetime
from tld import get_fld
from multiprocessing import Pool
from colorama import Fore, init
class getHost(object):
    def __init__(self, thread, web):
        self.thread = thread
        self.web = web

    init(convert=True,autoreset=True)

    def get(self, web):
        try:
            res = get_fld(web, fix_protocol=True)
            save = open('domain.txt', 'a')
            save.write('http://'+res+'\n')
            save.close()
            print(Fore.LIGHTBLUE_EX, '[+] http://{}'.format(res))
        except:
            pass

    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.get, self.web)
            worker.close()
            worker.join()
        return print('Saved As domain.txt')