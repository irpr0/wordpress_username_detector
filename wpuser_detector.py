#!/usr/bin/python
#  You can use from this code in your projects 
#  Developer : jok3r ~ Iran-cyber.net
import urllib2, re, os
from time import sleep

banner = '''

    ##      ## ########  
    ##  ##  ## ##     ## 
    ##  ##  ## ##     ## 
    ##  ##  ## ########  
    ##  ##  ## ##        
    ##  ##  ## ##        v 0.1 - For Developers
     ###  ###  ##        iran-cyber.net

	 Simple Wordpress username Detector.

	 Developer : Jok3r

	 telegram : @publish
	 
	 #! --> add http:// to your target !
'''


def cls():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

cls()

print (banner)

url = raw_input("Enter your target : ")

address = url + '/?author=1'
data = urllib2.urlopen(address).read()
req = re.findall("<title>(.*?)</title>", data)
user = re.search("(.*?) |", req[0]).group(1)
username = user

if user == "":
	username = "admin"

cls()
print (banner)
print '\n\n\033[1;33m[+] domain  : ' + url + '\033[1;m'
print '\033[1;33m[+] Username: ' + user + '\033[1;m'
sleep(3)
