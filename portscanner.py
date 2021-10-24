"""
    A minimalistic port-scanner in python

    ... that we might need in another project.
"""
import socket
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--ip", type=str, help="the ip address of the server")
parser.add_argument("--port", type=int, help="the port to scan")
parser.add_argument("--rangeFrom", type=int, help="range of ports to scan from")
parser.add_argument("--rangeTo", type=int, help="range of ports to scan to")

args = parser.parse_args()

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

if args.ip and args.port:
    print(scan_port(args.ip, args.port))

if __name__ == '__main__':
    scan_result = scan_port_range("199.247.5.104", 20, 85)
    for result in scan_result:
        if result['is_open']:
            print(f"{result['ip']} - {result['port']} = {result['is_open']}")



