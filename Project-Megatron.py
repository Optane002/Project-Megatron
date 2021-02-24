#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Project-Megatron is a another all in one project by Óptane. All the developments done by Óptane and some of the Megatron resources can forked from respective developers.


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which

print(G + '[+]' + C + 'Starting Project-Megatron...' + W)
print(G + '[+]' + C + 'Connecting with Óptane Servers' + W)
print(G + '[+]' + R + 'Obtaining for Dependencies' + W)
pkgs = ['python3', 'pip3', 'php', 'ssh']
inst = True
for pkg in pkgs:
    present = which(pkg)
    if present == None:
        print(R + '[-]' + W + pkg + C + 'is not Installed!')
        inst = False
    else:
        pass
if inst == False:
    exit()
else:
    pass

import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp

row = []
info = ''
result = ''
version = '1.0.0'

def banner():
    print (G +
    r'''
 _      ____  _____  _____  ______  ____  ____
| |    / __ ||  ___||  _  ||__  __|/ __ ||    |
| |    ||  ||| |    | |_| |  |  |  ||  |||   _|
| |___ ||__||| |___ |  _  |  |  |  ||__||| |\ \
|____ ||____/|_____||_| | |  |__|  |____/|_| \_\
     \/                  \/        ''' + W)
    print('\n' + G + '[>]' + C + 'Developed by : ' + W + 'Óptane(Chamicara.Desilva)')
    print(G + '[>]' + C + ' Current Version    : ' + W + version + '\n')

def ver_check():
    print(G + '[+]' + C + 'Megatron is Checking for Updates...', end='')
    ver_url = 'https://raw.githubusercontent.com/Optane002/Project-Megatron/main/version.txt?token=ALJ4HXW7KU4ULZLWIX2MHDLAG2TXG'
	try:
		ver_rqst = requests.get(ver_url)
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
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
        
def template_select():
	global site, info, result
	print(G + '[+]' + C + ' Select a Template : ' + W + '\n')
