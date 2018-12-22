
import subprocess
import sys
subprocess.call(["apt-get", "install", "apache2"])
subprocess.call(["apt-get", "install", "lynx"])
subprocess.call(["apt-get", "install", "wget"])
subprocess.call(["apt-get", "install", "curl"])

subprocess.call(["sudo", "cp", "/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/dominio1.conf"])

fin = open("/etc/apache2/sites-available/000-default.conf", 'r') # in file
fout = open("/etc/apache2/sites-available/dominio1.conf ", 'r+') # out file
for line in fin:
	if "DocumentRoot /var/www/html" in line :
		fout.write("\n ServerName dominio1.cdps \n ServerAlias www.dominio1.cdps \n")
	else:
		fout.write(line)

fin.close()
fout.close()
subprocess.call(["sudo", "a2ensite", "dominio1.conf"])
subprocess.call(["service" , "apache2", "reload"])

