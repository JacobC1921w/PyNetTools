# PyNetTools
A library of networking tools that you can use in your Python3 project

## Functions:
```
portScan(localIP, port, threads = 10, timeout = 0.1)
```
A simple multi-threaded port scanner, that scans all hosts on a subnet for a specific port, returns a list, of which you need to use `parsePortScan()` to comprehend
- `localIP`: Your machines local IP address (You can get it from `getPrivateIP()`)
- `port`: The port to scan
- `threads`: How many threads for mutli-threading
- `timeout`: Timeout for giving up on response

```
getPrivateIP()
```
Returns the current machines private IP address (`192.168.*.*`, `10.0.0.*` etc.)


```
getPublicIP()
```
Returns the current machines public IP address (The one you see from typing `Whats my IP` into Google)


```
isUp(IP, port, timeout = 0.1)
```
Checks if the specified IP address has the specified port open, returns boolean
- `IP`: The IP to check
- `port`: the port to scan
- `timeout`: Timeout for giving up on response


```
getMACAddress()
```
Returns the MAC address for the current machine

```
getHostName()
```
Returns the hostname for the current machine

```
parsePortScan(results, localIP)
```
- `results`: the list that you get from `portScan()`
- `localIP`: Your machines local IP address (You can get it from `getPrivateIP()`)

