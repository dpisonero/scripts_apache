import subprocess
import sys
webName = sys.argv[1]

# modificar /etc/hosts
fin = open("/etc/hosts", 'r+') # in file

for line in fin:
	if "127.0.0.1 localhost" in line :
		fin.write("\n 192.168.122.241 www." + webName + ".cdps \n")

fin.close()

#crear la página web
subprocess.call(["sudo", "mkdir", "/var/www/" + webName])
#subprocess.call(["sudo", "cp", "/var/www/html/index.html",  "/var/www/" + webName + "/index.html"])

fout = open("/var/www/" + webName + "/index.html", 'w')
fout.write("\n <html> \n <p> servidor " + webName + "</p> \n </html>")
fout.close()

# configurar el servidor
subprocess.call(["sudo", "cp", "/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/" + webName + ".conf"])

#fin = open("/etc/apache2/sites-available/000-default.conf", 'r') # in file
fout = open("/etc/apache2/sites-available/" + webName + ".conf", 'r+') # out file

for line in fout:
	if "DocumentRoot /var/www/html" in line :
		fout.write("DocumentRoot /var/www/" + webName)
		fout.write("\n ServerName " + webName + ".cdps") 
		fout.write("\n ServerAlias www." + webName + ".cdps \n")
	else:
		fout.write(line)

#fin.close()
fout.close()

subprocess.call(["sudo", "a2ensite", webName + ".conf"])
subprocess.call(["service" , "apache2", "reload"])

