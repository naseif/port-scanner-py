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
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--ip", type=str, help="the ip address of the server")
    parser.add_argument("--port", type=int, help="the port to scan")
    parser.add_argument("--rangeFrom", type=int, help="range of ports to scan from")
    parser.add_argument("--rangeTo", type=int, help="range of ports to scan to")

    args = parser.parse_args()

    if args.ip and args.port:
        print(scan_port(args.ip, args.port))
    
    if args.ip and args.rangeFrom and args.rangeTo:
        scan_results = scan_port_range(args.ip, args.rangeFrom, args.rangeTo)
        for result in scan_results:
            print(f"{result['ip']} - {result['port']} = {result['is_open']}")




