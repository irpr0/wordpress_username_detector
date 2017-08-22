import requests, re, sys, time, os, random
from colorama import Fore, Back, Style



def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """


    __          __           _
    \ \        / /          | | Iran-Cyber.NeT
     \ \  /\  / /__  _ __ __| |_ __  _ __ ___  ___ ___
      \ \/  \/ / _ \| '__/ _` | '_ \| '__/ _ \/ __/ __|
       \  /\  / (_) | | | (_| | |_) | | |  __/\__ \__ |
        \/  \/ \___/|_|  \__,_| .__/|_|  \___||___/___/
             Version 2.0      | | wprecon.com Project
                              |_|
                Wordpress Get_information V 2.0
                Welcome To Wordpress_project : )
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()

sess = requests.session()

try:
    __list = sys.argv[1]
except IndexError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'Script.py ' + Fore.WHITE + 'List.txt'
    print(Style.RESET_ALL)
    sys.exit()



try:
    with open(__list, 'r') as f:
        site = f.read().splitlines()
except IOError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'Script.py ' + Fore.WHITE + 'List.txt'
    print Fore.RED + '[-]' + Fore.YELLOW + ' ' + sys.argv[1] + Fore.WHITE + ' --> Not found !'

    print(Style.RESET_ALL)
    sys.exit()



for url in site:
    Check_wp = sess.get(url, timeout=10)
    if '/wp-content/' in Check_wp.text:
        __Get_page = sess.get('http://wprecon.com/#results', timeout=15)


        def get_WpNoncE():
            try:
                find = re.findall("<input type='hidden' name='csrfmiddlewaretoken' value='(.*)'", __Get_page.text)
                path = find[0].strip()
                return path
            except:
                pass


        __WpNonce = get_WpNoncE()

        __data_post = {'q': url,
                       'csrfmiddlewaretoken': __WpNonce
                       }

        Hunt_Wp = sess.post('http://wprecon.com/#results', data=__data_post, timeout=30)


        def get_SErver():
            try:
                find = re.findall('Server: <span style="font-weight: 700;">\n\n(.*)', Hunt_Wp.text)
                path = find[0].strip()
                return path
            except:
                pass


        def get_X_Powered_By():
            try:
                find = re.findall('tr><td>X-Powered-By: <span style="font-weight: 700;">\n\n(.*)', Hunt_Wp.text)
                path = find[0].strip()
                return path
            except:
                pass


        def get_Wp_version():
            try:
                find = re.findall('58px; color: red;">(.*)</span>', Hunt_Wp.text)
                path = find[0].strip()
                return path
            except:
                pass


        def get_Wp_Sv_ip():
            try:
                find = re.findall('IP Address: <span style="font-weight: 700;">\n\n(.*)', Hunt_Wp.text)
                path = find[0].strip()
                return path
            except:
                pass


        def get_Wp_Plugins_name():
            try:
                find = re.findall('</span></td><td><b>(.*)</b>', Hunt_Wp.text)
                return find
            except:
                pass


        def get_Wp_Username():
            try:
                find = re.findall('User ID 1 : <strong>\n\n(.*)', Hunt_Wp.text)
                path = find[0].strip()
                return path
            except:
                pass


        Hunt_wp_SErver = get_SErver()
        Hunt_wp_powered = get_X_Powered_By()
        Hunt_wp_version = get_Wp_version()
        Hunt_wp_sv_ip = get_Wp_Sv_ip()
        Hunt_wp_plugins_name = get_Wp_Plugins_name()
        Hunt_wp_Admin_UseRnaMe = get_Wp_Username()
        try:
            print Fore.RED + '    [+] ' + Fore.CYAN + 'url: ' + Fore.WHITE + url
        except:
            print Fore.RED + '    [-] ' + Fore.YELLOW + 'url: ' + url + Fore.WHITE + ' No URL !'
            break

        try:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'CMS       : ' + Fore.YELLOW + 'Wordpress'
            print Fore.RED + '       [+] ' + Fore.CYAN + 'Username  : ' + Fore.YELLOW + Hunt_wp_Admin_UseRnaMe
        except:
            print Fore.RED + '       [+] ' + Fore.YELLOW + 'Username  : ' + Fore.YELLOW + ' Not found'
        try:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'Server    : ' + Fore.YELLOW + Hunt_wp_SErver
        except:
            print Fore.RED + '       [+] ' + Fore.YELLOW + 'Server    : ' + Fore.YELLOW + ' Not found'
        try:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'Powered By: ' + Fore.YELLOW + Hunt_wp_powered
        except:
            print Fore.RED + '       [+] ' + Fore.YELLOW + 'Powered By: ' + Fore.YELLOW + ' Not Found'
        try:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'Version   : ' + Fore.YELLOW + Hunt_wp_version
        except:
            print Fore.RED + '       [+] ' + Fore.YELLOW + 'Version   : ' + Fore.YELLOW + ' Not found'
        try:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'IP Address: ' + Fore.YELLOW + Hunt_wp_sv_ip
        except:
            print Fore.RED + '       [+] ' + Fore.CYAN + 'IP Address: ' + Fore.YELLOW + ' Not found'
        try:
            print Fore.RED + '       [*] ' + Fore.CYAN + 'plugins   : '
            for x in Hunt_wp_plugins_name:
                print Fore.RED + '          [+] : ' + Fore.GREEN + x
        except:
            print Fore.RED + '       [*] ' + Fore.CYAN + 'plugins   : ' + Fore.YELLOW + ' Not found'

        #try:
        #    with open('Result.txt', 'a') as Hunt_result:
        #        Hunt_result.write('-----------------------------' + '\n' + ' url : ' + url + '\n' + 'Cms : ' + 'Wordpress' + '\n' + 'username: ' + Hunt_wp_Admin_UseRnaMe + '\n' + 'Server :' + Hunt_wp_SErver + '\n' + 'Powered By:' + Hunt_wp_powered + '\n' + 'Version :' + Hunt_wp_version + '\n' + 'IP Address: ' + Hunt_wp_sv_ip + '\n' + '-----------------------------')
        #except TypeError:
        #    pass
    else:
        print Fore.RED + '\n    [-] ' + Fore.CYAN + 'url: '+ Fore.RED + url + Fore.WHITE + ' ---> Not Wordpress'
else:
    pass