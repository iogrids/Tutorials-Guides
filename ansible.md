## Introduction

In ansible the main machine where you are doing the installation from is called control machine and other machines are called target machine

## Installation:

Ansible can be installed either using 
```
pip install ansible 
```
or 
```
apt-get ansible
```
  
## Hosts file
 
Say you have around 5 machines for which configuration has to be done first you will have to configure the hosts file in /etc/hosts in all the five machines (both control machine and target machines)

syntax: ipaddress domain name
Example:

```
192.168.43.198 one.example.com ubuntu
192.168.43.238 two.example.com python
``` 

Once the host file is configured, copy the file to all target machines as shown below

```
scp /etc/hosts jeril@192.168.43.238:/etc/
```

Finally make changes in /etc/ansible/hosts file as shown below. Here you mention all the target machines and the control machine

```
# MY MACHINES
[myservers]
one.example.com
two.example.com
```

Using ssh-keygen (You will have to do this all the machines for passwordless authentication between 2 machines)

```
ssh-keygen
ssh-copy-id -i jeril@192.168.43.238
```

## Using the ping module in ansible

```
syntax: ansible <machine-name> -module ping -username root -k(-k will prompt for the password)
ansible two.example.com -m ping -u root -k
```

## Ansible playbooks

Instead of writing individual commands, you can write a group of commands which can be executed in a remote machine using Ansible playbooks. Ansible playbooks is a YAML file.  

Ansible playbook has 3 sections

- Target section - Defines on which hosts playbook has to be executed
- Variable section - Define variables which can be used in playbooks
- Task section - List all modules that you intend to run

Example:
```
 
---
  - hosts: two.example.com        #Target section
    user: root                    
    vars:                         #Variable section  
     sample_warning: 'Welcome to \nLinux Tutorials'
    tasks:                        #Task section 
     - name: sample change
       copy:                       #Name of the module used here is copy. copy module copies files to remote location  
        dest: /etc/sample          
        content: "{{ sample_warning }}"
 ```
 
 Save the file as example.yml
 
 To run the file
 ```
 ansible-playbook example.yml
 ```
