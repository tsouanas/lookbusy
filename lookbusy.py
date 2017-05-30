#!/usr/bin/env python
# author: Thanos Tsouanas <thanos@tsouanas.org>
# version: 0.24

import os, sys, random, time
r = random.randrange

act = [
 'Calculating',
 'Reading',
 'Interpreting',
 'Searching for',
 'Analyzing',
 'Inspecting',
 'Parsing',
 'Scanning',
 'Clearing',
 'Allocating',
 'Syncing',
 'Synchronizing',
 'Comparing',
 'Building additional calls for',
 'Checking redirected permissions for',
 'Changing permissions of',
 'Checking',
 'Loading additional modules to handle local',
]

obj = [
 'variables',
 'shared memory',
 'libraries',
 'shared libraries',
 'memory',
 'disks',
 'hard drives',
 'physical memory',
 'swap memory',
 'files',
 'devices',
 'layers',
 'executable files',
 'additional options',
 'bytecode',
 'virtual memory',
 'encrypted data',
 'vinum drives',
 'little-endian bits',
 'system disk',
 'binary system calls',
 'logfiles',
 'modules',
 'kernel modules',
 'vectors',
 'matrices',
 'images',
 'clusters',
]

war = [
 'File "sysfoo.h" not present. Replacing includes with "sysbar.h".',
 'Function timeout!',
 'Core dumped!',
 'Segmentation fault.',
 'Possible off-by-one error detected.'
]


########
# functions

def echo(s):
    '''Echo s to the stdout, rightaway!'''
    sys.stdout.write(s)
    sys.stdout.flush()

def do_dots(speed,dots):
    '''Print the dots. Duh!'''
    chances = r(70)
    if (chances == 0):
        dots = 128 + r(512)
        speed = 0.0001

    # print the dots
    for i in range(dots):
        echo('.')
        chances = r(1000)
        if   (chances ==   0): sex = speed*6
        elif (chances <  920): sex = speed*0.001
        elif (chances <  980): sex = speed*0.01
        else: sex = speed*0.1
        time.sleep(sex)
        if (sex > 6): chances = r(5)
        else: chances = r(4000)
        if (chances < 4): echo('X.')

def cancel():
    '''Print cancelling message.'''
    echo("\nUSER ABORT!\nTrying to clean-up the mess")
    do_dots(0.1,r(400))
    echo("Clean!\n")


########
# main

try:
    os.system('clear')
    while(True):
        action = act[r(len(act))]
        object = obj[r(len(obj))]
        chances = r(100)

        echo( "%s %s..." % (action, object) )
        do_dots(r(64), r(32)+r(8))
        if   (chances < 95): echo( "Done.")
        elif (chances < 98): echo( "Skipping.")
        elif (chances < 99): echo( "XX.FAILED!")
        else:
            line = r(16000)
            warning = war[r(len(war))]
            echo( "!WARNING!: [line %d] %s" % (line,warning))
        echo("\n")
        time.sleep(0.1+r(42)/100.0)

except KeyboardInterrupt:
    cancel()
