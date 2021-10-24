"""
    A minimalistic port-scanner in python

    ... that we might need in another project.
"""
import socket
import sys

def scan_port(ip, port):
    """
        Scans the port using the simple tcp-connect method
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = (ip, port)
        sock.connect(server_address)
        return True
    except:
        pass
    finally:
        sock.close()

    return False

def scan_port_range(ip, fromPort, toPort):
    result = []
    for port in range(fromPort, toPort):
        result += [f"{ip} - {port} = {scan_port(ip, port)}"]

    return result    
    
if __name__ == '__main__':
   scan_port_range("199.247.5.104", 20, 85)




