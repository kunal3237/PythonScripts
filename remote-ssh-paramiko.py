"""
Expected output
_______________________________________
Please enter the password...: ********

Filesystem      Size  Used Avail Use% Mounted on
tmpfs           780M  2.8M  778M   1% /run
/dev/sda19      102G   92G  4.8G  96% /
tmpfs           3.9G   22M  3.8G   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
efivarfs         72K   17K   51K  26% /sys/firmware/efi/efivars
tmpfs           3.9G     0  3.9G   0% /run/qemu
/dev/sda2       256M   36M  221M  14% /boot/efi
tmpfs           780M  128K  780M   1% /run/user/1000

"""

import getpass4
import os
import paramiko

ssh_client=paramiko.client.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
"""
To remove "Server 'localhost' not found in known_hosts" error
"""
os.environ["MY_SSH"]=getpass4.getpass(prompt="Please enter the password...: ")
ssh_client.connect('localhost',username='kunal',password=os.environ["MY_SSH"])
command='df -Ph'
stdin, stdout, stderr = ssh_client.exec_command(command)
"""
The command’s input and output streams are returned as 
Python file-like objects representing stdin, stdout, and stderr.
"""
stdin.close()
#print((stdout.read()))
print((stdout.read().decode('ascii').strip("\n")))

ssh_client.close()
