import ipaddress

# Create IPv4 and IPv6 addresses
ipv4_addr = ipaddress.IPv4Address('192.168.1.1')
ipv6_addr = ipaddress.IPv6Address('2001:db8::1')

# Create IPv4 and IPv6 networks
ipv4_net = ipaddress.IPv4Network('192.168.1.0/24')
ipv6_net = ipaddress.IPv6Network('2001:db8::/64')

# Create IPv4 and IPv6 interfaces
ipv4_iface = ipaddress.IPv4Interface('192.168.1.2/24')
ipv6_iface = ipaddress.IPv6Interface('2001:db8::2/64')

# Print address and network information
print(f"IPv4 Address: {ipv4_addr}")
print(f"IPv6 Address: {ipv6_addr}")
print(f"IPv4 Network: {ipv4_net}")
print(f"IPv6 Network: {ipv6_net}")

# Print network and host parts of interfaces
print(f"IPv4 Interface Network: {ipv4_iface.network}")
print(f"IPv4 Interface Host: {ipv4_iface.ip}")
print(f"IPv6 Interface Network: {ipv6_iface.network}")
print(f"IPv6 Interface Host: {ipv6_iface.ip}")

# Check if addresses are in networks
print(f"IPv4 Address in Network: {ipv4_addr in ipv4_net}")  # True
print(f"IPv6 Address in Network: {ipv6_addr in ipv6_net}")  # True

# Iterate through hosts in a network
print("IPv4 Hosts in Network:")
for host in ipv4_net.hosts():
    print(host)

# Get the number of hosts in a network
print(f"IPv4 Network Host Count: {ipv4_net.num_addresses}")  # 256
print(f"IPv6 Network Host Count: {ipv6_net.num_addresses}")  # 18446744073709551616
