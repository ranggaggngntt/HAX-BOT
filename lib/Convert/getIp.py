import socket
from multiprocessing import Pool

class Converter(object):

    def __init__(self, web, thread):
        self.web = web
        self.thread = thread


    def Converter(self, web):
        try:
            ip = socket.gethostbyname(web)
            print('{}: {}'.format(web, ip))
            open('convert-ip.txt', 'a').write(ip+'\n')
        except Exception:
            pass
    
    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.Converter, self.web)
            worker.close()
            worker.join()
        return print('Result Saved as convert-ip.txt')