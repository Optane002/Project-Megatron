#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Project-Megatron is a another all in one project by Óptane. All the developments done by Óptane and some of the Megatron resources can forked from respective developers.

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which

print(G + '[+]' + C + 'Starting Project-Megatron')
print(G + '[+]' + C + 'Project-Megatron Version')

row = []
info = ''
result = ''
version = '1.0.0'

print(G + '[>]' + C + 'Version :' + W + Version + '\n')

def ver_check():
    print(G + '[+]' + C + ' Checking for Updates.....', end='')
    ver_url = 'https://raw.githubusercontent.com/Optane002/Project-Megatron/main/version.txt'
    try:
        ver_rqst = request.get(ver_url)
        ver_sc = ver_rqst.status_code
        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()

            if version == github_ver:
                print(C + '[' + G + ' Up-To-Date ' + C +']' + '\n')
            else:
                print(C + '[' + G + ' Available : {} '.format(github_ver) + C + ']' + '\n')
        else:
            print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
    except Exception as e:
        print('\n' + R + '[-]' + C + ' Exception :' + W + str(e))
