import requests
from multiprocessing import Pool
from colorama import Fore, init
class Scanner(object):

    def __init__(self, site, thread):
        self.site = site
        self.thread = thread

    init(convert=True, autoreset=True)

    def CheckLogin(self, site):
        try:
            wpLogin = requests.get(site+'/wp-login.php', timeout=10, verify=False, allow_redirects=False)
            if wpLogin.status_code == 200:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found WP-Login'.format(site))
                save = open('wordpress.txt', 'a')
                save.write(site+'\n')
                save.close()
            else:
                pass
        except Exception:
            pass

    def CheckAdmin(self, site):
        try:
            wpAdmin = requests.get(site+'/wp-admin', timeout=10, verify=False, allow_redirects=False)
            if wpAdmin.status_code == 200:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found WP-Admin'.format(site))
                save = open('wordpress.txt', 'a')
                save.write(site+'\n')
                save.close()
                return True
            else:
                return False
        except Exception:
            return False

    def CheckUpgrade(self, site):
        try:
            wpUpgrade = requests.get(site+'/wp-admin/upgrade.php', timeout=10, verify=False, allow_redirects=False)
            if wpUpgrade.status_code == 200:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found wp-admin/upgrade.php'.format(site))
                save = open('wordpress.txt', 'a')
                save.write(site+'\n')
                save.close()
                return True
            else:
                return False
        except Exception:
            return False

    def CheckReadme(self, site):
        try:
            wpUpgrade = requests.get(site+'/readme.html', timeout=10, verify=False, allow_redirects=False)
            if wpUpgrade.status_code == 200:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found /readme.html'.format(site))
                save = open('wordpress.txt', 'a')
                save.write(site+'\n')
                save.close()
                return True
            else:
                return False
        except Exception:
            return False
    def CheckLink(self, site):
        try:
            wpLinks = requests.get(site, timeout=10, verify=False, allow_redirects=False)
            if 'wp-' in wpLinks.text:
                print(Fore.LIGHTBLUE_EX, '[+] {} : Found wpLinks'.format(site))
                save = open('wordpress.txt', 'a')
                save.write(site+'\n')
                save.close()
                print(site)
                return True
            else:
                return False
        except Exception:
            return False
    def Scan(self, site):
        try:
            self.CheckLogin(site)
            self.CheckAdmin(site)
            self.CheckUpgrade(site)
            self.CheckReadme(site)
            self.CheckLink(site)
        except:
            print(Fore.LIGHTRED_EX, '[+] {} : Not Found'.format(site))
            save = open('unknown_cms.txt', 'a')
            save.write(site+'\n')
            save.close()
    
    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.Scan, self.site)
            worker.close()
            worker.join()
        return print('Saved As wordpress.txt')