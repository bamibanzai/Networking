import paramiko
import time

def ssh_connect():
        #Variables
        ip = input("Enter the IP address of Device: ")
        username = input("Enter the Terminal Username of Device: ")
        password = input("Enter the Terminal Password of Device: ")

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


if __name__ == '__main__':
        # Connect to router using method below
        ssh_connect()
