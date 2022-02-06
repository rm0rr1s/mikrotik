#!/bin/env python3

import sys
import os
from _ast import arg

import requests
import json

""" Define common variables """
helpArg = False
debugMode = False
listRegions = False
configureWireguard = True


""" Program Arguments"""
if len(sys.argv) > 1:
    if arg.lower() == "help":
        helpArg = True
    if arg.lower() == "debug":
        debugMode = True
    if arg.lower() == "listregions":
        listRegions = True
    if arg.lower() == "configure":
        configureWireguard = True

if helpArg:
    print("Commands")
    print("")
    print("PIAWireguard.py                  Runs script manually")
    print("PIAWireguard.py help             Help text (This)")
    print("PIAWireguard.py debug            Runs script with verbose output of the script")
    print("PIAWireguard.py listregions      Lists usable PIA regions for the script")
    print("PIAWireguard.py confugure        Configure/Reconfigure Wireguard interface")
    print("")
    sys.exit(0)


def printDebug(text):
    """
    Allows us to easily print debugging information when debug param is used.
    """
    if debugMode:
        print(text)


def checkConfig(key):
    if key in config:
        if config.get(key):
            val = config.get(key)
        else:
            print(f"The value for {key} is missing in {configFile}")
            sys.exit(5)
    else:
        print(f"{key} is missing in {configFile}")
        sys.exit(5)
    return val


if configureWireguard:
    configFile = os.path.join(sys.path[0], 'mikrotik.json')
    if os.path.isfile(configFile):
        config = json.loads(open(configFile, 'r').read())
        mikrotikHost = checkConfig('mikrotikHost')



