import subprocess
import sys

fout = open("/etc/network/interfaces", 'r+') # out file
for line in fout:
	if "source /etc/network/interfaces.d/*.cfg" in line :
		fout.write("auto eth0 \n iface eth0 inet static \n address 192.168.122.241 \n netmask 255.255.255.0 \n gateway 192.168.122.1 \n dns-nameservers 192.168.122.1 \n")
	else:
		fout.write(line)

