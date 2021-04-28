#!/usr/bin/env python3

import socket
from multiprocessing.dummy import Pool
from itertools import repeat
from requests import get
from uuid import getnode
from icmplib import ping as ICMPLibPing

def portScan(localIP, port, threads = 10, timeout = 0.1):
    localIP = '.'.join(localIP.split('.')[0:-1]) + '.'
    threadPool = Pool(threads)
    scanResults = threadPool.starmap(isUp, zip([localIP + str(i) for i in range(1, 256)], repeat(port), repeat(timeout)))
    threadPool.close()
    threadPool.join()
    hosts = []
    for i in range(0, len(scanResults)):
        if scanResults[i]:
            hosts.append(scanResults[i].split(':')[0])
    return hosts

def getOpenPorts(IP, portRangeStop = 65535, portRangeStart = 1, threads = 10, timeout = 1.5):
    threadPool = Pool(threads)
    scanResults = threadPool.starmap(isUp, [(IP, i, timeout) for i in range(portRangeStart, portRangeStop + 1)])
    threadPool.close()
    threadPool.join()
    hosts = []
    for i in range(0, len(scanResults)):
        if scanResults[i]:
            hosts.append(scanResults[i].split(':')[1])
    return hosts

def getPrivateIP():
    try:
        tempSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tempSocket.connect(("8.8.8.8", 80))
        IP = tempSocket.getsockname()[0]
        tempSocket.close()
        return IP
    except:
        return "127.0.0.1"

def getPublicIP():
    try:
        return get("https://api.ipify.org").text
    except:
        return "0.0.0.0"

def ping(IP, timeout = 0.1):
    if ICMPLibPing(str(IP), 1, 1, float(timeout), privileged=False).is_alive:
        return IP
    else:
        return False

def hostScan(localIP, threads = 10, timeout = 0.1):
    localIP = '.'.join(localIP.split('.')[0:-1]) + '.'
    threadPool = Pool(threads)
    scanResults = threadPool.starmap(ping, zip([localIP + str(i) for i in range(1, 256)], repeat(timeout)))
    threadPool.close()
    threadPool.join()
    hosts = []
    for i in range(0, len(scanResults)):
        if scanResults[i]:
            hosts.append(scanResults[i])
    return hosts

def isUp(IP, port, timeout = 0.1):
    try:
        tempSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempSocket.settimeout(timeout)
        tempSocket.connect((str(IP), int(port)))
        tempSocket.settimeout(None)
        tempSocket.close()
        return IP + ':' + str(port)
    except:
        return False

def getMACAddress():
    try:
        return ':'.join(hex(getnode()).replace("0x", "").upper()[i : i + 2] for i in range(0, 11, 2))
    except:
        return "00:00:00:00:00:00"

def getHostName():
    try:
        return socket.gethostname()
    except:
        return ""
