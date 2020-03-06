# [Web Administration & Design](https://alwinwoo.github.io/pages/web.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/web.md)

Like having a baby, setting up a small piece of cyberspace with your own domain name, unique email address and doing radical stuff on your own server can be a lot of fun.

Here are some steps that I have obtained from the Internet to help you along the way.

# Steps

## Preparations
- Plan your site
  - what is your site about? what are you going to put on it?
  - what is your budget / technical expertise?
- Choose a domain name
  - a name that represents your site
  - a name that is easy to remember, pronounce or spell
  - must it end with .com or something else?
  - a name that is available
  - http://data.iana.org/TLD/tlds-alpha-by-domain.txt
- Decide the type of hosting
  - what is your budget and level of technical expertise?
  - shared / dedicated hosting
  - DIY on the cloud
  - DIY in the office / at home

## Steps to set up your server on Google Cloud
- Hosting on the cloud
  - Create a GCloud instance
  - Obtain Static Address

## Steps to set up your server at home or in office
- Static or Dynamic DNS
- buying new / using old computers / whatever is available
- set up port forwarding rules for your router

## Pointing the Domain Name to your server
- Set up DNS on CloudFlare

## Setting up the Basics
- Allowing Access
  - Create SSH private and public keys
  ```code
  ssh-keygen -f <ssh file names> -t rsa -b 4096    
  Copy the public key to the server    
  Copy the ssh_key to subdirectory .ssh    
  ```  
  - Add public key into SSH server
  - https://www.ssh.com/ssh/keygen/
  - http://travistidwell.com/jsencrypt/demo/
  - https://wiki.filezilla-project.org/Howto/

- Installing server (Debian 9)
- Install and setup common modules (Apache / PHP / mysql / openSSH / sshfs)
  ```code
  sudo apt-get update
  sudo apt-get install apache2 php php-gd php7.0-gd mysql-server phpmyadmin mysql-client openssh-server sshfs
  sudo chown <user>:<user> /var/www -R
  ```
  - https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-debian
  - https://medium.freecodecamp.org/how-to-create-and-connect-to-google-cloud-virtual-machine-with-ssh-81a68b8f74dd
  - https://cloudkul.com/blog/lamp-installation-on-google-cloud/
- Install PHPmyadmin for mysql
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
    - https://www.tecmint.com/change-secure-phpmyadmin-login-url-page/
  - Hardening server security for PHPmyadmin
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
    - https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-debian-9

## Setting up other Stuff
- Set up the email server
- anti spam
- maintenance
- cron
- rsync to back-up your server to another remote server
```code
rsync -avz --delete --exclude '.git' --info=progress2 -e "ssh -p <port number>" <your-domain-name>:/var/www/ /var/www
```

# Others

- markdown scripts
- teamspeak
- remote view
- VPS

# References


