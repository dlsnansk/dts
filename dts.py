#!/usr/bin/env python3
# dts.py
# DTS - CLI utility that shows DATE-n-TIME on clear screen

import datetime as dt
import time as t
import sys, os

nv='\033[?25l'
v='\033[?25h'

def cl():
    os.system('cls'if os.name=='nt'else'clear')

def main():
    try:
        print(nv,end='')
        while True:
            cl()
            time=dt.datetime.now().strftime('%I:%M %p')
            date=dt.datetime.now().strftime('%m.%d.%Y')
            now=f'''
   {time}
  {date}'''
            print(now,end='\r')
            t.sleep(1)
            
    except KeyboardInterrupt:
        print(f'\n{v}DTS has been stopped')
        sys.exit()
    except Exception as e:
        print(f'\n{v}[ERROR] -> {e}')
        sys.exit()
main()
