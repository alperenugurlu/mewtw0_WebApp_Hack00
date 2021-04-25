import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


prCyan('''''''▌│█║▌║▌║ ₳Ⱡ₱ɆⱤɆ₦ Ʉ₲ɄⱤⱠɄ ║▌║▌║█│▌'
       '''''''''''''''''')


prLightPurple('''''''''''''''   Information Gathering Tool
''''''''''''''''')


def web_site():
        website = (input(prPurple('Please Enter Web Address Name (For Example http://domainname.com & https://domain.com): ')))
        return website

def ipaddr():
        ip_adress = (input(prPurple('Please Enter Ip Address (For Example 192.168.*.*): ')))
        return ip_adress



alperen = web_site()
ugurlu = ipaddr()

prGreen('''Scanning In Progress......
''')

prGreen('''''''\n𝕨𝕨𝕨.𝕝𝕚𝕟𝕜𝕖𝕕𝕚𝕟.𝕔𝕠𝕞/𝕚𝕟/𝕒𝕝𝕡𝕖𝕣𝕖𝕟-𝕦-𝟟𝕓𝟝𝟟𝕓𝟟𝟙𝟟𝟠/\n'
        '''''''')

def scan1():
        nmap= os.system('nmap -sS -sV -p- -A ' + ugurlu)
        print(nmap)

def scan2():
        dirb = os.system('dirb ' + '' + '' + alperen)
        print(dirb)

def scan3():
        gobuster = os.system('gobuster' + '  '+ 'dir' + '  ' + '-u' + ' ' + ' ' + alperen + ' ' + '-w' + '/usr/share/dirb/wordlists/big.txt')
        print(gobuster)

def scan4():
        theharvester = os.system('theHarvester' + '  ' + '-d' + '  ' + '  ' + alperen + ' ' + '-b' + ' ' + 'all')
        print(theharvester)

scan1()
scan2()
scan3()
scan4()




