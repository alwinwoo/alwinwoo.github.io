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

## 2a. Steps to set up your DIY server on Google / IBM Cloud
- Hosting on the cloud
  - [Create a GCloud Account](https://cloud.google.com/gcp/getting-started)
  - [Create a GCloud instance](https://cloud.google.com/compute/docs/instances/create-start-instance)
  - [Reserve a Static IP Address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address)
  - Set up port forwarding rules
- Hosting on IBM
  - [Dashboard](https://cloud.ibm.com/)
  - Set up Security Groups
  
## 2b. Steps to set up your DIY server at home or in office
- Static or Dynamic DNS
- buying new / using old computers / whatever is available
- set up port forwarding rules for your router

- Install share folders on VBox
  ```code
  1. Start up server
  2. Check kernel VERSION with 'uname -r'
  - search for headers using 'apt search linux-headers-$(uname -r)'
  3. Install dependencies with 'sudo apt-get -y install dkms build-essential linux-headers-VERSION'
  4. Reboot server
  5. "Devices -> Insert Guest Additions CD image"
  - mkdir /mnt/cdrom
  - mount /dev/cdrom /mnt/cdrom
  - cd /mnt/cdrom
  - sh ./VBoxLinuxAdditions.run --nox11
  6. If there is an error, copy the VBoxLinuxAdditions.run file onto the server
  7. Make it executable (chmod -x) and run it with root privileges (sudo sh ./VBoxLinuxAdditions.run --nox11)
  8. Reboot server
  9. Create mount location eg. /home/drive
  10. Mount drive with 'sudo mount -t vboxsf <shared name> /home/drive'
      To make mount persistent (make sure to do a snapshot before continuing)
  11. sudo nano /etc/fstab
  12. Add the following line to fstab (separated by tabs) and press Ctrl+O to Save.
    <shared folder>	<guest mount>	vboxsf	defaults	0	0
  13. sudo nano /etc/modules
    add vboxsf to the file and save
  14. reboot server
  ```
  - https://serverfault.com/questions/674974/how-to-mount-a-virtualbox-shared-folder
  - https://docs.bitnami.com/virtual-machine/faq/configuration/install-virtualbox-guest-additions/
  

## 3a. Basic Setup
- Installing your server OS 
  - Debian 9 Stretch
  - Debian 10 Buster
  - Ubuntu Server 18.04.4 LTS
  - Ubuntu Server 19.10
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

  - Change Server Timezone
  ```code
  sudo rm /etc/localtime 
  sudo ln -s /usr/share/zoneinfo/Singapore /etc/localtime 
  ```
  
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

## 3c. Node.JS and Socket.IO (Websockets)

  Socket.IO is not the same as websockets
  - <https://www.educba.com/websocket-vs-socket-io/>
  - <https://socket.io/docs/>

  ```code

  // install and check nodejs
  sudo apt-get install 
  sudo apt-get update
  sudo apt-get install git-core curl build-essential openssl libssl1.0-dev python
  
  curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
  
  // close and reopen the terminal
  nvm --version
  nvm install 9     // install stable version 32-bit...
  node --version
    
  // if error occurs
  nvm cache clear
  
  // list installed versions
  nvm ls
  ```
  - <https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/>
  - <https://github.com/nodejs/help/issues/1040>

  ```code
  npm install -g node-gyp express socket.io uuid
  ```
  npm list -g --depth=0         // list packages  -g is to install globally (good to use)
  npm uninstall <package-name>  // uninstall

  # Socket.IO Tutorials
  
  - <https://www.tutorialspoint.com/socket.io/socket.io_chat_application.htm>
  - <https://www.html5rocks.com/en/tutorials/websockets/basics/>
  - <https://socket.io/get-started/chat>
  - <https://dev.to/paolodelia99/build-a-simple-chat-app-with-node-js-and-socket-io-apk>

  combine apache2 server with node
  ```code
  // to enable proxy, go to apache site .conf file
  add the following before </VirtualHost>
  ProxyRequests on
  ProxyPass         /where-index.js-runs/ http://localhost:port/
  ProxyPassReverse  /where-index.js-runs/ http://localhost:port/
  ProxyPass         /nodejs              http://localhost:port/
  ProxyPassReverse  /nodejs              http://localhost:port/
  ProxyPass         /socket.io/          http://localhost:port/socket.io/
  ProxyPassReverse  /socket.io/          http://localhost:port/socket.io/
  ProxyPass         /socket.io/          ws://localhost:port/socket.io
  ProxyPassReverse  /socket.io/          ws://localhost:port/socket.io
  
  // the following modules need to be active for proxying
  sudo a2enmod proxy
  sudo a2enmod proxy_http
  sudo a2enmod proxy_balancer
  sudo a2enmod lbmethod_byrequests
  sudo systemctl restart apache2
  ```
  - <https://blog.cloudboost.io/get-apache-and-node-working-together-on-the-same-domain-with-javascript-ajax-requests-39db51959b79>

## 4. Content Curation
- client-side MD markdown
  - <http://strapdownjs.com/>
  - searching on a markdown page
    - http://naereen.github.io/StrapDown.js/example7.html

- MDwiki for markdown
  - install lighttpd (or apache)
  - <http://dynalon.github.io/mdwiki/#!index.md>

- PHP for Nginx
  ```code
  sudo apt-get install php-fpm
  // confirm fpm is loaded 
  sudo systemctl status php7.0-fpm.service
  find / \( -iname "php.ini" -o -name "www.conf" \)
  
  // with file paths, edit webserver details in /etc/nginx/sites-available
  
  location / {
        try_files $uri $uri/ /index.php$is_args$args;
  }

  location ~ \.php$ {
        incude snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.1-fpm.sock;
  }
  
  sudo nginx -t
  sudo service nginx reload

  check with phpinfo()
  
  ```
  - <https://www.linode.com/docs/web-servers/nginx/serve-php-php-fpm-and-nginx/>
  - <https://serversforhackers.com/c/php-fpm-and-nginx>

## 5. Securing Your Server
- One-stop Hardening - be careful though
  - <https://github.com/pratiktri/server_init_harden>
- Anti-Spam
- Secure fail2ban and Cloudflare
  - <https://guides.wp-bullet.com/integrate-fail2ban-Cloudflare-api-v4-guide/>
  - <https://serverfault.com/questions/285256/how-to-unban-an-ip-properly-with-fail2ban>
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

  - File Permissions on Linux
    - for files served on the web, it is best for your user account to be part of the www-data (if apache or nginx is running with that account) so that you can use 775 instead of 666 or 777.
    - depending on what you need, not only do you need to set permissions for the files themselves, you need to set permissions for the DIRECTORY that the files are in as well, otherwise you will not be able to write or delete files

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

- bash for terminal (allow up and down arrows as history)
  ```code
  chsh -s /bin/bash
  ```
- curl (for downloading of external urls)
  ```code
  Locate your PHP.ini file (php -i | grep 'php.ini')
  Open the PHP.ini in notepad.
  Search or find the following : ';extension=php_curl.dll'
  Uncomment this by removing the semi-colon ';' before it.
  Save and Close PHP.ini.
  Restart Apache (sudo systemctl restart apache)
  ```
- cron
- Email (STMP / IMAP) server
  ```code
  
  Check and set-up domain
  hostname -f (check host name)
  sudo hostnamectl set-hostname your-fqdn

  Mailgun settings for SMTP credentials
  (check setup - to modify DNS records)
  - login postmaster@domain.com + password
  stmp.mailgun.org

  Install postfix and dovecot for mail server
  sudo apt-get install apache2 php7
  sudo apt-get install postfix
  (choose internet site)
  (enter domain name)
  sudo service postfix restart
  sudo apt-get install dovecot-imapd dovecot-pop3d
  sudo service dovecot restart
  
  install web-based email client eg. squirrelmail
  wget https://sourceforge.net/projects/squirrelmail/files/stable/1.4.22/squirrelmail-webmail-1.4.22.zip
  unzip squirrelmail-webmail-1.4.22.zip
  sudo mv squirrelmail-webmail-1.4.22 /var/www/html/
  sudo chown -R www-data:www-data /var/www/html/squirrelmail-webmail-1.4.22/
  sudo chmod 755 -R /var/www/html/squirrelmail-webmail-1.4.22/
  sudo mv /var/www/html/squirrelmail-webmail-1.4.22/ /var/www/html/squirrelmail
  sudo perl /var/www/html/squirrelmail/config/conf.pl
  (edit server settings - 2)
  -> use smtp.mailgun.org, use port 465 for secure TLS, smtp login (with custom username and password)
  (allow "server-side sorting - general options 3 - true)
  access email by going to domain.com/squirrelmail

  Create Mail Users
  sudo useradd username
  sudo passwd username
  sudo mkdir -p /var/www/html/user_directory
  usermod -m -d /var/www/html/user_directory username
  sudo chown -R username:username /var/www/html/user_directory
  
  - https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/
  - https://www.linuxbabe.com/mail-server/setup-basic-postfix-mail-sever-ubuntu
  - https://www.linuxbabe.com/mail-server/secure-email-server-ubuntu-16-04-postfix-dovecot
  ```
  
- install Axigen Mail Server
  ```code
  download Axigen and install
  open the admin page as instructed
  Go to WebAdmin → Security and Filtering
  under router settings, put in the SMTP settings from mailgun 
  check DNS settings are correct
  send email to mail-tester.com to see how spammy is the email (change if need be) 
  ```
  - <https://www.axigen.com/documentation/installing-axigen-on-linux-p1409126>
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
- smb server for ios / windows network sharing
  ```code
  sudo apt-get install samba smbclient
  sudo cp /etc/samba/smb.conf /etc/samba/smb.conf_backup
  sudo grep -v -E "^#|^;" /etc/samba/smb.conf_backup | grep . > /etc/samba/smb.conf
  sudo systemctl restart smbd
  
  // add users to samba
  sudo smbpasswd -a <username>
  
  // edit smb.conf to allow home directories and sharing
  
  for full access - edit /etc/samba/smb.conf
  
  [public]
  comment = public anonymous access
  path = /var/samba/
  browsable =yes
  create mask = 0660
  directory mask = 0771
  writable = yes
  guest ok = yes
  
  save and restart samba
  ```
  - <https://linuxconfig.org/how-to-configure-samba-server-share-on-debian-9-stretch-linux>
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
  - Telegram and stock
    - <https://www.instructables.com/id/Transform-Raspberry-Pi-Into-a-Stock-Exchange-Monit/>
  
  - Log SSH details
    ```code
    sudo apt install build-essential gcc zlib1g-dev libssl-dev
    
    Compile the new SSH server
    OPENSSH=/opt/openssh2
    mkdir -p /opt/openssh2/dist/
    cd ${OPENSSH}
    wget http://zlib.net/zlib-1.2.11.tar.gz
    tar xvfz zlib-1.2.11.tar.gz
    cd zlib-1.2.11
    ./configure --prefix=${OPENSSH}/dist/ && make && make install
    cd ${OPENSSH}
    wget http://www.openssl.org/source/openssl-1.0.1e.tar.gz
    tar xvfz openssl-1.0.1e.tar.gz
    cd openssl-1.0.1e
    ./config --prefix=${OPENSSH}/dist/ && make && make install_sw
    cd ${OPENSSH}
    wget https://ftp.eu.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.2p1.tar.gz
    tar xvfz openssh-6.2p1.tar.gz
    cd openssh-6.2p1
    sed -e 's/struct passwd \* pw = authctxt->pw;/logit("Honey: Username: %s Password: %s", authctxt->user, password);\nstruct passwd \* pw = authctxt->pw;/' -i auth-passwd.c
    ./configure --prefix=${OPENSSH}/dist/ --with-zlib=${OPENSSH}/dist --with-ssl-dir=${OPENSSH}/dist/ && make && make install
    
    Start server
    /opt/openssh2/dist/sbin/sshd -f /opt/openssh2/dist/etc/sshd_config (remember to change away from port 22)
    grep -i honey /var/log/auth.log
    ```
    
    - <https://hackernoon.com/how-ive-captured-all-passwords-trying-to-ssh-into-my-server-d26a2a6263ec>

  - Virtual Host for Nginx
    - <https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04>
    
  - Security Tools
    - <https://geekflare.com/online-scan-website-security-vulnerabilities/>
    
  - Termux for Android Note 9
    - <https://wiki.termux.com/wiki/FAQ>
    - install ssh server
      - <https://wiki.termux.com/wiki/Remote_Access>
      - termux user = u0_a176
      - use 'passwd' to change password
    - Node JS
      - <https://steemit.com/utopian-io/@faisalamin/how-to-run-java-script-language-node-js-on-comman-line-andoid-termux-also-work-for-non-rooted-devices>
