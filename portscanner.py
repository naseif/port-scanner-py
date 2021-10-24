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
        print("- port " + str(port) + " is open")
        return True
    except:
        print("- port " + str(port) + " is closed or filtered")
        pass
    finally:
        sock.close()

    return False

def scanner(ip, fromPort, toPort):
    for port in range(fromPort, toPort):
        scan_port(ip, port)
    
if __name__ == '__main__':
    scanner("199.247.5.104", 20, 85)


