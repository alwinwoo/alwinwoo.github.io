# [Web Administration & Design](https://alwinwoo.github.io/pages/web.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/web.md)

Creating

# Steps

## Preparations

- Plan Your Site
  - what is your site about
  - what you're going to put on it
  - your budget / technical expertise
- Choose a domain name
  - a name that represents your site
  - a name that is easy to remember
  - a name that is available
  - end with .com or something else?

- Decide where to host your site
  - on the cloud
  - in the office / at home
  - budget / technical expertise

## Setting up on Google Cloud

- Set up DNS on CloudFlare
- Hosting on the cloud
  - Create a GCloud instance
  - Obtain Static Address

## Setting up on own Server
- port forwarding

## Setting up the Basics
- Allowing Access
  - Create SSH private and public keys
  ```code
  ssh-keygen -f <ssh file names> -t rsa -b 4096    
  Copy the public key to the server    
  Copy the ssh_key to subdirectory .ssh    
  ```  
  - Add public key into SSH server

- Install and setup common modules (Apache / PHP / mysql / openSSH / sshfs)

- Setting up the email server
- anti spam
- security
- maintenance
- cron

# Others

- markdown scripts
- teamspeak
- remote view
- VPS

# References

- https://www.ssh.com/ssh/keygen/
- http://travistidwell.com/jsencrypt/demo/
- https://wiki.filezilla-project.org/Howto/

