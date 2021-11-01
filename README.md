# port-scanner-py

A minimalistic port-scanner in python to check remote ports

# How to use

You can use port-scanner-py either as a library or CLI tool

## Library

```py
import portscanner

portscanner.scan_port(192.168.178.22, 22) ## Scan single port only
portscanner.scan_port_range(192.168.178.22, 20, 80) ## Scan all ports from 20 to 80
```

## CLI

Scan single port:
```
python3 portscanner.py --ip 192.48.80.31 --port 22
```

Scan ports based on range:
```
python3 portscanner.py --ip 192.48.80.31 --rangeFrom 22 --rangeTo 80
```
