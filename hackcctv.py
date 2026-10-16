import os
import time
import subprocess
from logos import *

def install_libraries():
    print('\x1b[1;96mInstalling library...')
    time.sleep(0.3)
    clear_terminal()
    print('\x1b[1;96mInstalling library....')
    time.sleep(0.3)
    clear_terminal()
    print('\x1b[1;96mInstalling library.....')
    time.sleep(0.3)

def install_dependencies():
    subprocess.run('pip install --upgrade pip', shell=True)
    try:
        import requests, re
    except ImportError:
        os.system('pip install requests')
        os.system('pip install re')
install_libraries()
install_dependencies()
clear_terminal()
while True:
    type_text(chois)
    user_input = input(f'{green}$/> {blue}Enter a number :{pink} ')
    if user_input.isdigit():
        choice = int(user_input)
        if choice == 1:
            clear_terminal()
            import requests
            import re
            import time
            from logos import *
            try:
                type_text(timeline)
                x = ['+00:00', '+01:00', '+02:00', '+03:00', '+03:30', '+04:00', '+05:00', '+05:30', '+06:00', '+07:00', '+07:00', '+08:00', '+09:00', '+10:00', '+11:00', '+13:00', '-', '-02:00', '-03:00', '-04:00', '-05:00', '-06:00', '-07:00', '-08:00', '-09:00', '-10:00']
                num = int(input(f'\n{yellow}[?]~>{red}inter code timezone : '))
                if num not in range(1, 26):
                    raise IndexError
                text = ''
                time = x[num - 1]
                res = requests.get(f'http://www.insecam.org/en/bytimezone/{time}', headers=headers)
                last_page = re.findall('pagenavigator\\("\\?page=", (\\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get(f'http://www.insecam.org/en/bytimezone/{time}/?page={page}', headers=headers)
                    find_ip = re.findall('http://\\d+\\.\\d+\\.\\d+\\.\\d+:\\d+', res.text)
                    print(f'\n{bold + yellow}@DeadByte.dll')
                    print(green + '')
                    for ip in find_ip:
                        print(ip)
            except:
                print(red + ' !ERORR❌ ')
        elif choice == 2:
            clear_terminal()
            from logos import *
            import requests, re
            try:
                type_text(loc_n)
                loc = ['Server', 'Farm', 'Restaurant', 'Park', 'Brid', 'Beach', 'Bridge', 'Sport', 'Shop', 'Airline', 'Hotel', 'hq', 'Village', 'Road', 'Pool', 'Surfing', 'Parking', 'Traffic']
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
                num = int(input(f'\n{yellow}[?]~>{red}inter a number : '))
                if num not in range(1, 19):
                    raise IndexError
                text = ''
                loc = loc[num - 1]
                res = requests.get(f'http://www.insecam.org/en/bytag/{loc}', headers=headers)
                last_page = re.findall('pagenavigator\\("\\?page=", (\\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get(f'http://www.insecam.org/en/bytag/{loc}/?page={page}', headers=headers)
                    find_ip = re.findall('http://\\d+.\\d+.\\d+.\\d+:\\d+', res.text)
                    print(f'\n{bold + yellow}@DeadByte.dll')
                    print(green + '')
                    for ip in find_ip:
                        print(ip)
            except:
                print(red + ' !ERORR❌ ')
        elif choice == 3:
            clear_terminal()
            from logos import *
            import requests, re

            def type_text(text):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.0005)
                print()
            try:
                type_text(coun_n)
                countries = ['US', 'JP', 'IT', 'KR', 'FR', 'DE', 'TW', 'RU', 'GB', 'NL', 'CZ', 'TR', 'AT', 'CH', 'ES', 'CA', 'SE', 'IL', 'PL', 'IR', 'NO', 'RO', 'IN', 'VN', 'BE', 'BR', 'BG', 'ID', 'DK', 'AR', 'MX', 'FI', 'CN', 'CL', 'ZA', 'SK', 'HU', 'IE', 'EG', 'TH', 'UA', 'HK', 'GR', 'PT', 'MY', 'TN', 'NZ', 'BD', 'PA', 'MD', 'NI', 'MT', 'TT', 'SA', 'HR', 'CY', 'PK', 'AE', 'KZ', 'KW', 'GE', 'SV', 'LU', 'PR', 'CR', 'BY', 'AL', 'LI', 'BA', 'PY', 'PH', 'FO', 'GT', 'NP', 'PE', 'UY', 'AD', 'AG', 'AM', 'AO', 'AU', 'AW', 'AZ', 'BB', 'BS', 'BW', 'CG', 'CI', 'DZ', 'GA', 'GL', 'GP', 'GU', 'GY', 'HN', 'JM', 'JO', 'KE', 'KH', 'KN', 'KY', 'LA', 'LB', 'LK', 'MA', 'MG', 'MK', 'MN', 'MO', 'MQ', 'MU', 'NA', 'NC', 'NG', 'QA', 'RE', 'SD', 'SN', 'SR', 'ST', 'SY', 'TZ', 'UG', 'UZ', 'VC', 'BJ']
                num = int(input(f'{yellow}[?]~>{red}inter code country : '))
                if num not in range(1, 128):
                    raise IndexError
                text = ''
                country = countries[num - 1]
                res = requests.get(f'http://www.insecam.org/en/bycountry/{country}', headers=headers)
                last_page = re.findall('pagenavigator\\("\\?page=", (\\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get(f'http://www.insecam.org/en/bycountry/{country}/?page={page}', headers=headers)
                    find_ip = re.findall('http://\\d+.\\d+.\\d+.\\d+:\\d+', res.text)
                    print(f'\n{bold + yellow}@DeadByte.dll')
                    print(green + '')
                    for ip in find_ip:
                        print(ip)
            except:
                print(red + ' !ERORR❌ ')
        elif choice == 4:
            clear_terminal()
            import requests, re
            from logos import *
            green = '\x1b[1;92m'
            cyan = '\x1b[1;96m'
            yellow = '\x1b[1;93m'
            magenta = '\x1b[1;95m'
            white = '\x1b[1;97m'
            blue = '\x1b[1;94m'
            red = '\x1b[1;91m'
            underline = '\x1b[4m'
            pink = '\x1b[35m'
            bold = '\x1b[1m'
            black = '\x1b[30m'
            try:
                type_text(cam_n)
                MFs = ['DLink', 'DLink-DCS-932', 'TPLink', 'Foscam', 'Linksys', 'Sony', 'Sony-CS3', 'Vije', 'Mobotix', 'Panasonic', 'Megapixel', 'ChannelVision']
                num = int(input(f'\n{yellow}[?]~>{red}inter a number : '))
                if num not in range(1, 13):
                    raise IndexError
                text = ''
                MF = MFs[num - 1]
                res = requests.get(f'http://www.insecam.org/en/bytype/{MF}', headers=headers)
                last_page = re.findall('pagenavigator\\("\\?page=", (\\d+)', res.text)[0]
                for page in range(int(last_page)):
                    res = requests.get(f'http://www.insecam.org/en/bytype/{MF}/?page={page}', headers=headers)
                    find_ip = re.findall('http://\\d+.\\d+.\\d+.\\d+:\\d+', res.text)
                    print(f'\n{bold + yellow}@DeadByte.dll')
                    print(green + '')
                    for ip in find_ip:
                        print(ip)
            except:
                print(red + ' !ERORR❌ ')
    else:
        print(f'{red}Please enter a number')
    go_back = input(f'{bold}{yellow}Do you want to step out of the tool?!  {green}n{white} / {red}y{blue} {white}: ')
    if go_back.lower() not in ['no', 'n']:
        print(f"{red}FUCK THE NSA, FUCK THE ATF, FUCK THIS WHOLE WORLD")
        break
    else:
        clear_terminal()
