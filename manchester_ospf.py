import paramiko
import time


#Variables
ip = '192.168.3.1'
username = 'admin'
password = 'cisco'

#create SSH object
remote_ssh = paramiko.SSHClient()

#add untrusted hosts to SSH
remote_ssh.set_missing_host_key_policy(
paramiko.AutoAddPolicy())

# SSH Connect
remote_ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print"SSH connection established to %s" % ip

#Interactive Shell
ssh_shell = remote_ssh.invoke_shell()
print"Interactive SSH Session Available"

#Fetch Router Prompt
output = ssh_shell.recv(1000)
print output

#Commands
ssh_shell.send("enable\n")
ssh_shell.send("cisco\n") #line con 0 password
ssh_shell.send("conf t\n")
ssh_shell.send("router ospf 1\n")
ssh_shell.send("network 192.168.3.0 0.0.0.255 area 0\n")
ssh_shell.send("network 172.16.3.0 0.0.0.3 area 0\n")
ssh_shell.send("network 172.16.2.0 0.0.0.3 area 0\n")
ssh_shell.send("exit\n")
ssh_shell.send("end\n")
ssh_shell.send("show ip protocols\n")

#Wait for command to complete
time.sleep(2)

#Receive Command outputs
output = ssh_shell.recv(5000)
print output


