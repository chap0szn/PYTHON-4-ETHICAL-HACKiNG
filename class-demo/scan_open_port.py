#Importing a module

import socket
import argparse

#Create a Socket object
def scan_port(ip, port):
    """check if a specific port is open on a given ip address."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set a timeout for connection attempt
        sock.settimeout(1)
        
        #Try connecting to IP addr & Port number
        result = sock.connect_ex((ip, port))

        #If condition statement
        if result == 0:
            print(f"[+] Port {port} is open on {ip}")
        else:
            print(f"[-] Port {port} is closed on {ip}")
        sock.close()
    except Exception as e:
        print(f"[-]Error scanning port {port} on {ip}")

def scan_ports(ip, start_port, end_port):
    """scan a range of ports on a given ip address"""
    print(f"\n scanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

#The main program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this tool was created by WebDeves CyberSec Team")
    parser.add_argument("ip",help="Target IP address")
    parser.add_argument("--start",type=int, default=1, help="specify starting port (default:1)")
    parser.add_argument("--end", type=int, default=1024, help="specify the ending port (default:1024)")

    args = parser.parse_args()

    scan_ports(args.ip, args.start, args.end)

