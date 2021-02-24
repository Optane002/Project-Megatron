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

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Provide Subdomain for Serveo URL ( Optional )')
parser.add_argument('-k', '--kml', help='Provide KML Filename ( Optional )')
parser.add_argument('-t', '--tunnel', help='Specify Tunnel Mode [ Available : manual ]')
parser.add_argument('-p', '--port', type=int, default=8080, help='Port for Web Server [ Default : 8080 ]')

args = parser.parse_args()
subdom = args.subdomain
kml_fname = args.kml
tunnel_mode = args.tunnel
port = args.port

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
