
import socket
from multiprocessing.dummy import Pool
from itertools import repeat
from requests import get
from uuid import getnode

def portScan(localIP, port, threads = 10, timeout = 0.1):
	localIP = '.'.join(localIP.split('.')[0:-1]) + '.'
	threadPool = Pool(threads)
	scanResults = threadPool.starmap(isUp, zip([localIP + str(i) for i in range(1, 256)], repeat(port), repeat(timeout)))
	threadPool.close()
	threadPool.join()
	return scanResults

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

def isUp(IP, port, timeout = 0.1):
	try:
		tempSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tempSocket.settimeout(timeout)
		tempSocket.connect((str(IP), int(port)))
		tempSocket.settimeout(None)
		tempSocket.close()
		return True
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

def parsePortScan(results, localIP):
	hostsUp = []
	hostsDown = []
	localIP = '.'.join(localIP.split('.')[0:-1]) + '.'

	for i in range(0, len(results)):
		if results[i]:
			hostsUp.append(localIP + str(i + 1))
		else:
			hostsDown.append(localIP + str(i + 1))
	return hostsUp, hostsDown

if __name__ == "__main__":
    print("MAC Address:\t" + getMACAddress())
    print("Private IP:\t" + getPrivateIP())
    print("Public IP:\t" + getPublicIP())
