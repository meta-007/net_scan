import socket
import time
from scapy.all import *
import scapy.all as scapy
from scapy import *

start = time.time()

def get_mac(ip):

 ##    scapy.arping(ip)
 ## Let creat arp packet
    try:
        arp_request = scapy.ARP(pdst = ip)
 ##        arp_request.show()
 ##        scapy.ls(scapy.ARP())
        broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
 ##        broadcast.show()
 ##        scapy.ls(scapy.Ether())
        arp_broadcast = broadcast/arp_request
 ##        arp_broadcast.show()
        ans = scapy.srp(arp_broadcast,timeout=1,verbose=False)[0]
        return ans[0][1].hwsrc
    except IndexError:
        pass
## port scanning fuction


### here we are scanning port
target = input("Enter IP Address to scan > ")
ports = int(input("Enter the port numbers to be scanned: "))
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target) 

def port_scan(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:      
        s.connect((target_ip,port))
        return True
    except:
        return False

for port in range(ports):## enter the port number till you want to scan or specify the port number
    if port_scan(port):
        print(f"port {port} is open")
        break
    else:
        print(f"port {port} is closed")

mac_address = get_mac(target)
print("[+] Target ip addrress " + target +"\n"+ " MAC Address "+ str(mac_address))   

end = time.time()
print(f"Time taken {end-start:.2f} seconds")

