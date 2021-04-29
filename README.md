# PyNetTools
A library of networking tools that you can use in your Python3 project

## Functions:

### Port Scanning
```python
portScan(localIP, port, threads = 10, timeout = 0.1)
```
A simple multi-threaded port scanner, that scans all hosts on the subnet for a specific port, returns a list (ret: array)
- `localIP`: (str) Your machines local IP address (You can get it from `getPrivateIP()`)
- `port`: (int) The port to scan
- `threads`: (int) How many threads for mutli-threading
- `timeout`: (float) Timeout for giving up on response

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.portScan(PyNetTools.getPrivateIP(), 80)
['192.168.0.1']
>>> 
```

<br />
<br />

### Portscanning specific host
```python
getOpenPorts(IP, portRangeStop = 65535, portRangeStart = 1, threads = 10, timeout = 1.5)
```
Returns all open ports between the specified `portRangeStop` and `portRangeStart`. NOTE: I've found the best and most accurate results come from setting `timeout=1.5`, but it may differ from person to person (ret: int array)
- `IP`: (str) The target IP to scan
- `portRangeStop`: (int) The port to stop scanning at
- `portRangeStart`: (int) The port to commence scanning at
- `threads`: (int) The amount of threads to use while portscanning
- `timeout`: (float) The timout for checking if port is open (SEE ABOVE)

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getOpenPorts("192.168.0.1", 100)
[53, 80]
>>>
```

<br />
<br />

### Portscanning specific host (with list of ports)
```python
getOpenPortsFromList(IP, portList, threads = 10, timeout = 1.5)
```
Returns all open ports within `portList`. (ret: int array)
- `IP`: (str) The target IP to scan
- `portList`: (int list) list of integers to scan
- `threads`: (int) The amount of threads to use while portscanning
- `timeout`: (float) The timeout for checking if port is open

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getOpenPortsFromList("192.168.0.1", [80, 22, 21, 8008])
[80]
>>>
```

<br />
<br />

### Getting Private IP
```python
getPrivateIP()
```
Returns the current machines private IP address (`192.168.*.*`, `10.0.0.*` etc.) (ret: str)

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getPrivateIP()
'192.168.0.1'
>>> 
```

<br />
<br />

### Getting Public IP
```python
getPublicIP()
```
Returns the current machines public IP address (The one you see from typing `Whats my IP` into Google) (ret: str)

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getPublicIP()
'123.123.123.123'
>>> 
```

<br />
<br />

### Chekcing Whether Host Is Online
```python
ping(IP, timeout = 0.1)
```
Checks if the specified IP address is online using unprivileged ICMP packets (ret: str if online, bool if offline)
- `IP`: (str) The IP to check
- `timeout`: (float) Timeout for giving up on response

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.ping("192.168.0.1") # Is online
"192.168.0.1"
>>> PyNetTools.ping("192.168.0.2") # Isn't online
False
>>>
```

<br />
<br />

### Host Scanning
```python
hostScan(localIP, threads = 10, timeout = 0.1)
```
A simple multi-threaded host scanner, that sends unprivileged ICMP packets to all hosts on the subnet, returns a list (ret: array)
- `localIP`: (str) Your machines local IP address (You can get it from `getPrivateIP()`)
- `threads`: (int) How many threads for mutli-threading
- `timeout`: (float) Timeout for giving up on response

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.hostScan(PyNetTools.getPrivateIP())
['192.168.0.1', '192.168.0.3', '192.168.0.133', '192.168.0.147', '192.168.0.224']
>>> 
```

<br />
<br />

### Checking Whether Port Is Open
```python
isUp(IP, port, timeout = 0.1)
```
Checks if the specified IP address has the specified port open (ret: str if up, False if not)
- `IP`: (str) The IP to check
- `port`: (int) the port to scan
- `timeout`: (float) Timeout for giving up on response

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.isUp("192.168.0.1", 80) # Is up
"192.168.0.1:80"
>>> PyNetTools.isUp("192.168.0.2", 80) # Isn't up
False
>>>
```

<br />
<br />

### Getting MAC Address
```python
getMACAddress()
```
Returns the MAC address for the current machine (ret: str)

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getMACAddress()
'A4:B1:C1:FD:B2:2C'
>>>
```

<br />
<br />

### Getting Machine Hostname
```python
getHostName()
```
Returns the hostname for the current machine (ret: str)

#### Example:
```python
>>> import PyNetTools
>>> PyNetTools.getHostName()
'Arch'
>>>
```

