#!/bin/bash

echo "<h1 id="id1" >Hostname :  </br> $(hostname)</h1>" > index.html
/usr/sbin/apache2 -D FOREGROUND

#!/bin/bash
sudo su
apt update -y
apt install -y httpd
systemctl start httpd.service
echo "<h1> sgn ons </h1>" > /var/www/html/sgn.html
 