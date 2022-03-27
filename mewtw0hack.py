import os

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


prCyan('''
                                _                 ___  
                               | |               / _ \ 
  _ __ ___     ___  __      __ | |_  __      __ | | | -|
 | '_ ` _ \   / _ \ \ \ /\ / / | __| \ \ /\ / / | | |----|
 | | | | | | |  __/  \ V  V /  | |_   \ V  V /  | |_| --|
 |_| |_| |_|  \___|   \_/\_/    \__|   \_/\_/    \___/ 
                                                       
                                                                                                                         
            ▌│█║▌║▌║ ₳Ⱡ₱ɆⱤɆ₦ Ʉ₲ɄⱤⱠɄ ║▌║▌║█│▌''' )
            
            

prLightPurple('''''''''''''''
Web Application Information Gathering & Enumeration Tool
''''''''''''''')


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
        
        
def scan00():
		whois = os.system('whois' + '' + alperen)

def scan1():
        nmap= os.system('nmap' + ' ' + '-sS' + ' ' + '-Pn' + ' ' + '-T4' + ' ' + '-p-' + ' ' + '-vv' + ' ' + ugurlu)
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
def scan5():
		dirsearch = os.system('dirsearch' + ' ' + '-u' + ' ' + alperen + ' ')
		print(dirsearch)
def scan6():
		metagoofil = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'xsl')
		print(metagoofil)
def scan7():
		metagoofil2 = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'docx')
		print(metagoofil2)
def scan8():
		metagoofil3 = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'pdf') 
		print(metagoofil3)
def scan9():
		metagoofil4 = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'csv')
		print(metagoofil4)
def scan10():
		metagoofil5 = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'txt')
		print(metagoofil5)
def scan11():
		metagoofil6 = os.system('metagoofil' + ' ' + '-d' + ' ' + alperen + ' ' + 't' + ' ' + 'xml')
		print(metagoofil6)	
def scan12():
		subfinder = os.system('subfinder' + ' ' + '-d' + ' ' + alperen + ' ')
		print(subfinder)
		

scan00()
scan2()
scan3()
scan4()
scan5()
scan6()
scan7()
scan8()
scan9()
scan10()
scan11()
scan12()
scan1()
