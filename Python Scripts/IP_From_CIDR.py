import ipaddress

ip = ipaddress.IPv4Address('192.168.1.1')

net = ipaddress.IPv4Network('192.168.1.0/24')

ipv4_iface = ipaddress.IPv4Interface('192.168.1.2/24')

print(ipv4_iface)

print(ip in net)
