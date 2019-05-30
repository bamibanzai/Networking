import paramiko
import time

def ssh_connect():
        # Variables
        # Set IP of router here
        ip = '192.168.1.1'
        username = 'admin'
        password = 'cisco'

        # Create SSH object
        remote_ssh = paramiko.SSHClient()

        #add untrusted hosts to SSH
        remote_ssh.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())

        # SSH Connect
        remote_ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
        print"SSH connection established to %s" % ip

        # Interactive Shell
        ssh_shell = remote_ssh.invoke_shell()
        print"Interactive SSH Session Available"

        # Fetch Router Prompt
        output = ssh_shell.recv(1000)
        print output

        # Commands
        ssh_shell.send("enable\n")
        ssh_shell.send("conf t\n")
        ssh_shell.send("router rip\n")
        ssh_shell.send("version 2\n")
        ssh_shell.send("network 172.16.1.2\n")
        ssh_shell.send("network 172.16.3.1\n")
        ssh_shell.send("show ip route\n")

        # Wait for command to complete
        time.sleep(2)

        # Receive Command outputs
        output = ssh_shell.recv(5000)
        print output

if __name__ == '__main__':
        # Connect to router using method below
        ssh_connect()
