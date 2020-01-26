import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst='')
    print(arp_request.summary())
    # scapy.ls(arp_request)

scan('')




