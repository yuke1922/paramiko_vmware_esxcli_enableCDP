import paramiko
from getpass import getpass
import re

vm_pass = getpass("Enter Host Password: ")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='172.19.60.34', username='root', password=vm_pass)

ssh_client.exec_command("esxcli network vswitch standard set --cdp-status=both -v vSwitch0")
