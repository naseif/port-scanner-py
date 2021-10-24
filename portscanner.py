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
    """
        scan a port range and return a list of ports and their states
    """
    result = []
    for port in range(fromPort, toPort):
        result += [dict(
            ip = ip,
            port = port,
            is_open = scan_port(ip, port)
        )]
    return result    
    
if __name__ == '__main__':
    scan_result = scan_port_range("199.247.5.104", 20, 85)
    for result in scan_result:
        if result['is_open']:
            print(f"{result['ip']} - {result['port']} = {result['is_open']}")



