#!/bin/python
from os import system
from platform import system as sm
typeSystem : str = sm()
try:
    from requests import post,get
except ModuleNotFoundError or ImportError:
    system('pip3 install requests')
	from requests import post,get
from random import randint, choice
from json import loads, dumps, JSONDecodeError
import base64,urllib3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from time import sleep, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class clients:
	web = {
		"app_name"    : "Main",
		"app_version" : "3.2.1",
		"platform"    : "Web",
		"package"     : "web.rubika.ir",
		"lang_code"   : "fa"
	}

	android = {
		"app_name"    : "Main",
		"app_version" : "2.8.1",
		"platform"    : "Android",
		"package"     : "ir.resaneh1.iptv",
		"lang_code"   : "fa"
	}
defaultDevice = {
	"app_version":"MA_2.9.8",
	"device_hash":"CEF34215E3E610825DC1C4BF9864D47A",
	"device_model":"rubika-library",
	"is_multi_account": False,
	"lang_code":"fa",
	"system_version":"SDK 22",
	"token":"cgpzI3mbTPKddhgKQV9lwS:APA91bE3ZrCdFosZAm5qUaG29xJhCjzw37wE4CdzAwZTawnHZM_hwZYbPPmBedllAHlm60v5N2ms-0OIqJuFd5dWRAqac2Ov-gBzyjMx5FEBJ_7nbBv5z6hl4_XiJ3wRMcVtxCVM9TA-",
	"token_type":"Firebase"
}
class encryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('UTF-8'), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result

class robot:
    def __init__(self, auth=None, device=defaultDevice):
        if auth != None:
            self.auth = auth
        self.enc = encryption(self.auth)
    @staticmethod
    def auths():
        auths = ""
        choices = [*"abcdefghijklmnopqrstuvwxyz"]
        for i in range(32): auths += choice(choices)
        return auths
    @staticmethod
    def url():
        server = ['https://messengerg2c37.iranlms.ir/', 'https://messengerg2c64.iranlms.ir/', 'https://messengerg2c26.iranlms.ir' ,'https://messengerg2c46.iranlms.ir' ,'https://messengerg2c39.iranlms.ir']
        host : str = (choice(server))
        return host
    def block(self, guid):
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"setBlockUser",
            "input":{
                "action": "Block",
                "user_guid": guid
            },
            "client": clients.web
        }))},url=robot.url()).json()["data_enc"]))
    def reportObject(self, user,  mode):
        return loads(self.enc.decrypt(post(json={
            "api_version":"4",
            "auth": self.auth,
            "client": clients.android,
            "data_enc":self.enc.encrypt(dumps({
                "object_guid": user,
                "report_description": mode, 
                'report_type_object': 'Object', 
                'report_type': 100,
            })),
            "method":"reportObject"
        },url=robot.url()).json()["data_enc"]))
class run:
    def running():
		if 'linux' in typeSystem.lower() or 'mac' in typeSystem.lower():
			system('clear')
		else:
			system('cls')
        numb : int = input('\n\033[31m[?] \033[36mplease enter number report \033[31m_> \033[0m')
        number = int(numb)
        num : int = 0
        method : str = input('\n\033[31m[?] \033[36moh! "1" for your auth , oh! "2" for random auth\n\n\033[92mplease enter method \033[31m_> \033[0m')
        if method == '1':
            auth : str = input('\n\033[31m[?] \033[36mplease enter your AUTH \033[31m_> \033[0m')
        guid : str = input('\n\033[31m[?] \033[36mplease enter guid target _> \033[0m')
        # MODE FOR REPORT !
        the : str = input('\n\033[31m[?] \033[36mmode report \033[31m\'0\' \033[36mfor spam \033[31\'1\' \033[36mfor your file codes list \033[31m_> \033[20;37m')
        if the == '0':
            mode : str = 'مستهجن'
        if the == '1':
            mod : str = input('\n\033[31m[?] \033[36mplease enter file codes list \033[31m_> \033[0m')
            mode = open(mod ,'r').read().split('\n')
        with open('auths.txt', 'w') as create:
            create.write('')
        if the == '1':
            while num < number:
                sleep(1.5)
                date : str = time()
                if method == '2':
                    auth : str = robot.auths()
                bot = robot(auth=auth)
                try:
                    bot.block(guid)
                except:
                    pass
                try:
                    bot.reportObject(user=guid, mode=mode)
                    print(f'\n\033[31m[1] \033[36mauth \033[31m/ \033[92mTrue \033[31m/\033[36m {auth}')
                    with open('auths.txt', 'a') as true:
                        true.write(auth+'\n')
                except:
                    print(f'\n\033[31m[1] \033[36mauth \033[31m/ \033[35mFalse \033[31m/\033[36m {auth}')
                num += 1
        else:
            for code in mode:
		date : str = time()
                sleep(1.5)
                if method == '2':
                    auth : str = robot.auths()
                bot = robot(auth=auth)
                try:
                    bot.block(guid)
                except:
                    pass
                try:
                    bot.reportObject(user=guid, mode=code)
                    print(f'\n\033[31m[1] \033[36mauth \033[31m/ \033[92mTrue \033[31m/\033[36m {auth} \033[31m/ \033[93mcode: \033[92m{code} \033[31m/ \033[92m{date}')
                    with open('auths.txt', 'a') as true:
                        true.write(auth+'\n')
                except:
                    print(f'\n\033[31m[1] \033[36mauth \033[31m/ \033[35mFalse \033[31m/\033[36m {auth} \033[31m/ \033[93mcode: \033[92m{code} \033[31m/ \033[92m{date}')
# ........... START ............
if __name__ == '__main__':
    run.running()
else:
    raise TypeError('[!] SUPPORT -> @creator_ryson')
