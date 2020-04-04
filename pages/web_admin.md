# [Web Administration - Server](https://alwinwoo.github.io/pages/web_admin.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/web_admin.md)

Like having a baby, setting up your small corner of cyberspace using your own domain name with a unique email address, doing radical stuff on your own server can be a lot of fun.

Here are some steps from the Internet that I have summarised to help you along the way.

# Steps

## 1. Preparations
- Plan your site
  - what is your site about? what are you going to put on it?
  - what is your budget / technical expertise? (<span style="color:red">if you don't understand the article below, I suggest you proceed with caution</span>)
    - <https://github.com/imthenachoman/How-To-Secure-A-Linux-Server>
- Choose a domain name
  - a name that represents your site
  - a name that is easy to remember, pronounce or spell (must it end with .com or something else?)
  - a name that is available
    - <http://data.iana.org/TLD/tlds-alpha-by-domain.txt>
- Decide the type of hosting
  - what is your budget and level of technical expertise?
    - DIY server on the cloud eg. Google Cloud, AWS
    - DIY server in the office / at home
      - Linux or Windows?
      - <https://github.com/imthenachoman/How-To-Secure-A-Linux-Server>

## 2a. Steps to set up your DIY server on Google Cloud
- Hosting on the cloud
  - [Create a GCloud Account](https://cloud.google.com/gcp/getting-started)
  - [Create a GCloud instance](https://cloud.google.com/compute/docs/instances/create-start-instance)
  - [Reserve a Static IP Address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address)
  - Set up port forwarding rules
  
## 2b. Steps to set up your DIY server at home or in office
- Static or Dynamic DNS
- buying new / using old computers / whatever is available
- set up port forwarding rules for your router

## 3a. Basic Setup
- Installing your server OS 
  - Debian 9/10, Ubuntu
- Pointing the Domain Name to your DIY server
  - Set up DNS on [CloudFlare](https://www.cloudflare.com)
    ```code
    NS - ara.ns.cloudflare.com
    NS - pablo.ns.cloudflare.com
    A - domain name - ip address - Auto - Proxied (or DNS only)
    A - sub-domain  - ip address (can be different) - Auto - Proxied (or DNS only)
    ```
- Install commonly-used modules (Apache / PHP / mysql / openSSH / sshfs)
  ```code
  sudo apt-get update
  sudo apt-get install apache2 php php-gd php7.0-gd mysql-server phpmyadmin mysql-client openssh-server sshfs
  sudo chown <user>:<user> /var/www -R
  ```
  - <https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-debian>
  - <https://medium.freecodecamp.org/how-to-create-and-connect-to-google-cloud-virtual-machine-with-ssh-81a68b8f74dd>
  - <https://cloudkul.com/blog/lamp-installation-on-google-cloud/>
- Securing Access
  - Create SSH private and public keys (puttygen?)
  - Save the ppk file in a secure location
  - Add public key into SSH server
  - <https://www.ssh.com/ssh/keygen/>
  - <http://travistidwell.com/jsencrypt/demo/>
  - <https://wiki.filezilla-project.org/Howto/>

## 3b. Setup as bigbluebutton server
- Create instance server (Ubuntu 16.04 LTS) 4 core 8GB memory w 100GB storage
  - assign static address
  - add firewall rules (I use bigblue) 
    - TCP/IP port 22 (for SSH)
    - TCP/IP ports 80/443 (for HTTP/HTTPS)
    - UDP ports in the range 16384 - 32768 (for FreeSWITCH/HTML5 client RTP streams)
- create domain name that you want to use the server in cloudflare (requires SSL for mic and video)
```code
A - sub-domain  - ip address (can be different) - Auto - Proxied (or DNS only)
```
- Install bigbluebutton
  ```code
  sudo -s
  wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s <your-domain-name> -e <your-email-address> -a -g
  wait for 10-15 minutes
  ```
- Install Greenlight Accounts
  ```code
  cd greenlight/
  Default Admin: docker exec greenlight-v2 bundle exec rake admin:create
  Admin: docker exec greenlight-v2 bundle exec rake user:create["name","email","password","admin"]
  User: docker exec greenlight-v2 bundle exec rake user:create["name","email","password","user"]
  ```
- Setup BBB
  - go to organiszation settings with admin account and change Site Settings as desired
    - Branding image, Registration Method, Authentication, Number of Rooms
- <https://github.com/bigbluebutton/bbb-install>

## 4. Content Curation
- MDwiki for markdown
  - install lighttpd (or apache)
  - <http://dynalon.github.io/mdwiki/#!index.md>

## 5. Securing Your Server
- One-stop Hardening - be careful though
  - <https://github.com/pratiktri/server_init_harden>
- Anti-Spam
- .htaccess for PHPmyadmin
    ```code
    Secure phpmyadmin with .htaccess
    sudo nano /etc/apache2/conf-available/phpmyadmin.conf
    <add AllowOverride All under DirectoryIndex index.php>
    sudo systemctl restart apache2
    sudo nano /usr/share/phpmyadmin/.htaccess
    <add 
    AuthType Basic
    AuthName "Restricted Files"
    AuthUserFile /etc/phpmyadmin/.htpasswd
    Require valid-user
    >
    sudo htpasswd -c /etc/phpmyadmin/.htpasswd username
    sudo htpasswd /etc/phpmyadmin/.htpasswd additionaluser
    ```
   - <https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-debian-9>
- login URL for PHPmyadmin
  ```code
  sudo mysql -u root -p
  create user 'username'@'localhost' identified by 'password';
  (SUPER USER RIGHTS) grant all privileges on *.* to 'username'@'localhost' with grant option;
  sudo /etc/init.d/apache2 restart
  sudo /etc/init.d/mysql restart
  sudo ln -s /usr/share/phpmyadmin /var/www/html
  <set up the rest of the users on <url/phpMyAdmin>
  SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('newpassword'); (Change Password)
  Phpmyadmin config files are located in /etc/apache2/conf-enabled and /etc/phpmyadmin/
  $cfg['Servers'][$i]['controluser'] = 'pma'; 
  $cfg['Servers'][$i]['controlpass'] = '';
  sudo nano /etc/phpmyadmin/apache.conf
  ```
    - <https://www.tecmint.com/change-secure-phpmyadmin-login-url-page/>

## 6. Maintaining your DIY server
  - Add users and change passwords
    ```code
    adduser <name>
    passwd <name>
    ```
  - Add users with chroot
    ```code
    usermod -d /var/www/myApplication/ exampleuser
    ```
    - <https://www.tecmint.com/restrict-ssh-user-to-directory-using-chrooted-jail/>
    - <https://askubuntu.com/questions/961231/how-to-change-default-ftp-directory-in-linux>
  - Add users to sudoers
    ```code
    usermod -aG sudo <user name>
    ```
    - <https://linuxize.com/post/how-to-create-a-sudo-user-on-debian/>
  - Reset mysql root password
    ```code
    sudo /etc/init.d/mysql stop
    sudo mysqld_safe --skip-grant-tables &
    mysql -uroot
    use mysql;
    update user set authentication_string=PASSWORD("mynewpassword") where User='root';
    flush privileges;
    quit
    sudo /etc/init.d/mysql stop
    sudo /etc/init.d/mysql start
    mysql -u root -p
    Enter your new password when prompted.
    ```
    - <https://support.rackspace.com/how-to/mysql-resetting-a-lost-mysql-root-password/>
  - Change PHP upload directory
    - edit /etc/php/7.0/apache2/php.ini

# 7. Others - Useful but may not be necessary

- curl (for downloading of external urls)
  ```code
  Locate your PHP.ini file
  Open the PHP.ini in notepad.
  Search or find the following : ';extension=php_curl.dll'
  Uncomment this by removing the semi-colon ';' before it.
  Save and Close PHP.ini.
  Restart Apache.
  ```
- cron
- Email server
- FTP server (why would you want to do this if you have SSH?)
  - <https://www.thomas-krenn.com/en/wiki/Setup_FTP_Server_under_Debian>
- git
- Remote view
  ```code
  sudo apt install xfce4 xfce4-desktop xfce4-goodies xorg dbus-x11 x11-xserver-utils
  sudo apt install xrdp
    => check with 'sudo systemctl status xrdp'
  sudo systemctl enable xrdp
  sudo adduser xrdp ssl-cert 
  sudo nano /etc/xrdp/xrdp.ini
    => add 'exec startxfce4' at end of file
  sudo systemctl restart xrdp
  => open port 3389 (GCloud is 'default-allow-rdp')
  ```
  - <https://linuxize.com/post/how-to-install-xrdp-on-ubuntu-18-04/>
  - <https://linoxide.com/linux-how-to/xrdp-connect-ubuntu-linux-remote-desktop-via-rdp-from-windows/>
- rsync to back-up your server to another remote server
  ```code
  rsync -avz --delete --exclude '.git' --info=progress2 -e "ssh -p <port number>" <your-domain-name>:/var/www/ /var/www
  ```
- SSL certificate
  ```code
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 3650 (self-signed)
  sudo mv cert.pem /etc/ssl/certs/
  sudo mv key.pem /etc/ssl/private/
  sudo a2ensite default-ssl (enables website - a2dissite disables the site)
  sudo nano /etc/apache2/sites-enabled/default-ssl.conf
  sudo a2enmod ssl (enables modules)
  sudo /etc/init.d/apache2 restart
  ```
  - <https://www.sslshopper.com/apache-server-ssl-installation-instructions.html>
- teamspeak
- VPS

# 8. Stuff I'm Trying 
- lighttpd with markdown
  ```code
  sudo apt-get install php cgi rubygems build-essential ruby-dev libfcgi-dev
  sudo gem update --system
  sudo gem install rack bluecloth ruby-fcgi
  sudo wget https://raw.githubusercontent.com/theirix/fcgi-markdown/master/fcgi-markdown.fcgi
  sudo lighttpd-enable-mod fastcgi fastcgi-php
  sudo nano /etc/lighttpd/lighttpd.conf 
  +++++
  fastcgi.server = (".md" => ((
    "bin-path" => "/var/www/fcgi-markdown.fcgi",
    "kill-signal" => 10,
    "port" => 1027))
  )
  +++++
  sudo lighttpd-enable-mod cgi fastcgi
  sudo service lighttpd reload
  ```
  - https://github.com/theirix/fcgi-markdown/blob/master/README.md
