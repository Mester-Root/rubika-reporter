#!/bin/python
from os import system; from platform import system as sm; from time import sleep, time; from random import choice
try: from rubx import rubx
except ModuleNotFoundError or ImportError:
    system('pip3 install rubx')
    from rubx import rubx
try: from pyfiglet import figlet_format
except ModuleNotFoundError or ImportError:
    system('pip3 install pyfiglet')
    from pyfiglet import figlet_format
typeSystem : str = sm()
class run:
    api_hash: list = []
    def running():
        if 'linux' in typeSystem.lower() or 'mac' in typeSystem.lower(): system('clear')
        else: system('cls')
        logo : list = ['rubika . ir', 'rubika', 'r-ubika', 'rEpOrTeR']; banners : str = (choice(logo)); banner : str = figlet_format(banners)
        [(print('\033[92m'+bnr, flush=True, end=''), sleep(0.008)) for bnr in banner]
        number, method = int(input('\n\033[31m[?] \033[36mplease enter number report \033[31m_> \033[0m')), str(input('\n\033[31m[?] \033[36moh! "1" for your auth , oh! "2" for random auth\n\n\033[92mplease enter method \033[31m_> \033[0m'))
        if method == '1':
            auth : str = input('\n\033[31m[?] \033[36mplease enter your AUTH \033[31m_> \033[0m')
            run.api_hash.append(auth)
        guid, the = input('\n\033[31m[?] \033[36mplease enter guid target _> \033[0m'), input('\n\033[31m[?] \033[36mmode report \033[31m\'0\' \033[36mfor spam \033[31m\'1\' \033[36mfor your file codes list \033[31m_> \033[20;37m')
        if the == '0':
            mode : str = 'مستهجن'
        elif the == '1':
            mod : str = input('\n\033[31m[?] \033[36mplease enter file codes list \033[31m_> \033[0m')
            try:
                mode = open(mod ,'r').read().split('\n')
            except:
                while 1:
                    try:
                        print(f'\n\033[31m[!] \033[35mFile \033[31m{mod} \033[35mNotFound\n')
                        mod : str = input('\n\033[31m[?] \033[36mplease enter file codes list \033[31m_> \033[0m'); mode = open(mod ,'r').read().split('\n')
                        break
                    except:
                        pass
            for code in mode:
                date : str = time()
                sleep(1.5)
                if method == '2':
                    auth : str = str(rubx.Bot.auths())
                    bot = rubx.Bot('md', auth=auth, welcome=False)
                else:
                    bot = rubx.Bot('md', auth=run.api_hash[0], welcome=False)
                try:
                    assert bot.block(guid)
                except:
                    pass
                try:
                    bot.reportObject(user=guid, mode=code)
                    print(f'\n\033[31m[+] \033[36mauth \033[31m/ \033[92mTrue \033[31m/\033[36m {auth} \033[31m/ \033[93mcode: \033[92m{code} \033[31m/ \033[92m{date}')
                except:
                    print(f'\n\033[31m[!] \033[36mauth \033[31m/ \033[35mFalse \033[31m/\033[36m {auth} \033[31m/ \033[93mcode: \033[92m{code} \033[31m/ \033[92m{date}')
        for i in range(int(number)):
            sleep(1.5)
            date : str = str(time())
            if method == '2':
                auth : str = str(rubx.Bot.auths())
                bot = rubx.Bot('md', auth=auth, welcome=False)
            else:
                bot = rubx.Bot('md', auth=run.api_hash[0], welcome=False)
            try:
                assert bot.block(guid)
            except:
                pass
            try:
                bot.reportObject(guid, mode)
                print(f'\n\033[31m[+] \033[36mauth \033[31m/ \033[92mTrue \033[31m/\033[36m {auth} \033[31m/ \033[93mreport: \033[92m[SPAM] \033[31m/ \033[92m{date}')
            except:
                print(f'\n\033[31m[!] \033[36mauth \033[31m/ \033[35mFalse \033[31m/\033[36m {auth} \033[31m/ \033[93mreport: \033[92m[SPAM] \033[31m/ \033[92m{date}')
# ........... START ............
if __name__ == '__main__':
    try:
        run.running()
    except:
        pass
else:
    raise TypeError('[!] SUPPORT -> @creator_ryson')
