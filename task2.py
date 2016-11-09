import re

ips = {}

file = open('access.log', 'r')

for line in file:
    caught_ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
    for ip in caught_ips:
        subnet = ".".join(ip.split(".")[:3])
        if subnet in ips:
            if ip not in ips[subnet]:
                ips[subnet].append(ip)
        else:
            ips[subnet] = [ip]

for subnet, ip_list in ips.items():
    print(subnet, " : ", ip_list)