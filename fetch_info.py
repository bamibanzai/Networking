import paramiko
import time
import re
import os
import sqlite3
from itertools import islice


class Router_Connect():
        def __init__(self, ip, username, password):
                self.ip = ip
                self.username = username
                self.password = password
        def ssh_connect(self):

                #create SSH object
                remote_ssh = paramiko.SSHClient()

                #add untrusted hosts to SSH
                remote_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # SSH Connect
                remote_ssh.connect(self.ip, username=self.username, password=self.password, look_for_keys=False, allow_agent=False)
                print"SSH connection established to %s" % self.ip


                #Interactive Shell
                ssh_shell = remote_ssh.invoke_shell()
                print"Interactive SSH Session Available"

                #Fetch Router Prompt
                output = ssh_shell.recv(1000)
                print output

                '''Fetch IOS VERSION'''
                ssh_shell.send("show version\n")
                # Wait for command to complete
                time.sleep(1)

                # Receive Command outputs
                output2 = ssh_shell.recv(5000)

                # File Saving
                print'Writing Version info to file...'
                fileInfo = output2.strip()
                writefile1 = open('version.txt', 'w')
                writefile1.write(fileInfo)
                writefile1.write('\n')
                writefile1.close()


                '''Fetch IP ROUTE INFO'''
                ssh_shell.send("\n")
                ssh_shell.send("show ip route\n") #IP ROUTE

                # Wait for command to complete
                time.sleep(1)

                # Receive Command outputs
                output1 = ssh_shell.recv(5000)

                #File Saving
                fileInfo = output1.strip()

                writefile2 = open('ip_route.txt', 'w')
                writefile2.write(fileInfo)
                writefile2.write('\n')
                writefile2.close()

                database = "router.db"
                connection = sqlite3.connect(database)
                print'Database connected...'
                print'Writing Routing info to db...'
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS routing (name VARCHAR(16), info VARCHAR(16))''')
                sql_cmd = "REPLACE INTO routing (name, info) VALUES(?,?)"

                ip_route_list =[]
                file2 = open('ip_route.txt', 'r')
                for line in file2:
                        line_output = re.search("[0-9].+\.[0-9].+\.[0-9].+\.[1-9].*\/[0-9][0-9]", line)
                        if line_output:
                                ether = re.search("FastEthernet[0-9]\/[0-9]", line)
                                serial = re.search("Serial[0-9]\/[0-9]", line)
                                if ether or serial:
                                        g = line_output.group()
                                        e = ether.group()
                                        s = serial.group()
                                        ip_route_list.append(e)
                                        ip_route_list.append(g)
                                        ip_route_list.append(s)
                                        cursor.execute(sql_cmd, (ip_route_list[0], ip_route_list[1], ip_route_list[2]))
                                        file2.close()

                                else:
                                        continue
                        else:
                                continue

                os.remove('ip_route.txt')
                connection.commit()


                '''Fetch VLAN Info'''
                ssh_shell.send("\n")
                ssh_shell.send("show vlans\n")
                # Wait for command to complete
                time.sleep(1)

                # Receive Command outputs
                output3 = ssh_shell.recv(5000)

                # File Saving
                fileInfo = output3.strip()
                print'Writing VLAN info to file...'
                writefile3 = open('vlan.txt', 'w')
                writefile3.write(fileInfo)
                writefile3.write('\n')
                writefile3.close()


                '''Fetch CPU Processes'''
                ssh_shell.send("show processes cpu\n")
                # Wait for command to complete
                time.sleep(1)

                # Receive Command outputs
                output4 = ssh_shell.recv(5000)

                # File Saving
                fileInfo = output4.strip()

                writefile4 = open('processes.txt', 'w')
                writefile4.write(fileInfo)
                writefile4.write('\n')
                writefile4.close()

                database = "router.db"
                connection = sqlite3.connect(database)
                print'Database connected...'
                print'Writing processes info to db...'
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS cpu (PID VARCHAR(16), Runtime VARCHAR(16), Invoked VARCHAR(16), uSecs VARCHAR(16), Sec VARCHAR(16), MinOne VARCHAR(16), MinFive VARCHAR(16), TTY VARCHAR(16), Process VARCHAR(16))''')

                file4 = open('processes.txt', 'r')
                for a in islice(file4, 3, 10):
                        sql_cmd = "REPLACE INTO cpu (PID, Runtime, Invoked, uSecs, Sec, MinOne, MinFive, TTY, Process) VALUES(?,?,?,?,?,?,?,?,?)"
                        b = a.strip().split()
                        cursor.execute(sql_cmd, (b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]))
                        connection.commit()

                file4.close()
                os.remove('processes.txt')

                #End connection to database
                cursor.close()
                connection.close()


print"Router Information includes: Routing Table, CPU Running Processes, iOS Version, VLAN Information\n"

if __name__ == '__main__':
        ip = input("Enter the IP address of Device: ")
        user = input("Enter the Terminal Username of Device: ")
        passwd = input("Enter the Terminal Password of Device: ")
        router = Router_Connect(ip, user, passwd)
        info = router.ssh_connect()

