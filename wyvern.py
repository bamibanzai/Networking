#CROSS-COMPATIBILITY BETWEEN PYTHON 2 & 3
from __future__ import (absolute_import, division, print_function, unicode_literals)

# CMP5321 Programming module - Ron Austin - Birmingham City University#
#  Comparison of network device configurations script#

# Package/Libraries list
import sys # Needed for error handling function, retrieves system data. and for sys.exit()
import os       # Needed for some os functions.
import time     # Needed for slowing down some sections where human interaction need apply.
from colorama import Fore, Style  # Color text output because why not.
import paramiko # SSH package, the Python community seems to think it's slightly better replacement for pexpect.


class WyvernAgent(object): # Main class everything outside of this class is secondary.
    def main_menu(self):
        print("=================================================")
        print("Wyvern: Python comparison agent | [Version]: 0.24")
        print("=================================================")
        print(Fore.YELLOW + '''        
 _    _                                  
| |  | |                                 
| |  | | _   _ __   __  ___  _ __  _ __  
| |/\| || | | |\ \ / / / _ \| '__|| '_ \ 
\  /\  /| |_| | \ V / |  __/| |   | | | |
 \/  \/  \__, |  \_/   \___||_|   |_| |_|
          __/ |                          
         |___/                           
        ''' + Style.RESET_ALL)
        print_statement("Options: 1), Quit: 2)")
        try:
            answer = int(input("(Wyvern):> "))
        except ValueError:
            exception_trap()
            return
        return answer

    def main_menu_settings(self): # This function is responsible for controlling the main menu.
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                try:
                    print('''
                           [Help commands]
                           main         | Task agent to exit back to menu.
                           kill         | Task agent to exit to shell.
                           system info  | Task agent to get system information.
                           version      | Task agent to get software version.
                           rip          | Task agent to configure RIP V2 on routers.
                           show diff     | Task agent to compare running config with NVRAM.
                           show running | Task agent to compare current with offline version.
                           ''')


                    print_statement("Which help command would you like to run? ")
                    help_command = str(input("(Wyvern):> "))


                    if help_command == 'main': # Returns user to the main menu
                        loop = 1
                        os.remove("tmp.log") # Removes old tmp file


                    elif help_command == 'kill':
                        os.remove("tmp.log") # Removes old tmp file
                        system_exit()


                    elif help_command == 'system info':
                        os.system("uname") # Uses built in command uname to get system name
                        print("\n")
                        time.sleep(2)
                        os.system("cat /etc/*release*")


                    elif help_command == 'version':
                        wyvern_credits()


                    elif help_command == 'rip':
                        print_statement("Type the IP address of the router you want to select.")
                        print("HQ Router: 192.168.1.1") 
                        print("Bristol Router: 192.168.2.1")
                        print("Manc Router: 192.168.3.1")


                        another_loop = str(input("Please select an IP: "))


                        if another_loop == "192.168.1.1":
                            print_statement("Selected 192.168.1.1")


                        elif another_loop == "192.168.2.1":
                            print_statement("select 192.168.2.1")


                        elif another_loop == "192.168.3.1":
                            print_statement("select 192.168.3.1")

                        else:
                            print_statement("It appears you've entered the error IP address, exiting.....")
                            system_exit()

                        M = another_loop
                        get_router_ip(M)
                        print_statement("Please stand by, retrieving details. ")
                        time.sleep(2)
                        os.system("cat tmp.log")
                        print("\n")

                        rip_config = str(input("(Wyvern):> yes/no Confirmation, Would you like to configure RIP V2 for this device?  "))

                        if rip_config == "yes":
                            print("\n")
                            print(Fore.RED + "(Wyvern):> WARNING: Accepting will automatically run through a preset of commands to configure RIP V2 on " '%s' % M + " device." + Style.RESET_ALL)
                            print("\n")

                        elif rip_config == "no":
                            print_statement("Returning you to main menu")
                            time.sleep(2)
                            loop = 1

                        rip_confirmation = str(input(Fore.YELLOW + "(Wyvern):> yes/no Confirmation, Are you absolutely sure? " + Style.RESET_ALL))

                        if rip_confirmation == "yes":
                            print_statement("Please stand by.")
                            time.sleep(2)
                            paramiko_rip_config(M)
                            return


                        elif rip_confirmation == "no":
                            time.sleep(2)
                            system_exit()


                        else:
                            print_statement("You have not entered a compatible command, please try again.")
                            system_exit()


                    elif help_command == 'show diff':
                            print_statement("Type the IP address of the router you want to select.")
                            print("HQ Router: 192.168.1.1") 
                            print("Bristol Router: 192.168.2.1")
                            print("Manc Router: 192.168.3.1")

                            yetanotherloop = str(input("Please select an IP: "))

                            if yetanotherloop == "192.168.1.1":
                                print_statement("Selected 192.168.1.1")


                            elif yetanotherloop == "192.168.2.1":
                                print_statement("Selected 192.168.2.1")


                            elif yetanotherloop == "192.168.3.1":
                                print_statement("Selected 192.168.3.1")


                            else:
                                print_statement("It appears you've entered the error IP address, please try again.")
                                system_exit()

                            H = yetanotherloop
                            get_router_ip(H)
                            print_statement("Please stand by, retrieving details. ")
                            time.sleep(2)
                            os.system("cat tmp.log")
                            print("\n")
                            running_config = str(input("(Wyvern):> yes/no Confirmation, Would you like to run the command Show run for this device?  "))


                            if running_config == "yes":
                                print("\n")
                                print(Fore.RED + "(Wyvern):> WARNING: Accepting will automatically run through a preset of commands on " '%s' % H + " device." + Style.RESET_ALL)
                                print("\n")


                            elif running_config  == "no":
                                time.sleep(2)
                                system_exit()


                            running_config_confirmation = str(input(Fore.YELLOW + "(Wyvern):> yes/no Confirmation, Are you absolutely sure? " + Style.RESET_ALL))


                            if running_config_confirmation == "yes":
                                print_statement("Please stand by.")
                                time.sleep(2)
                                paramiko_running_config(H)
                                return


                            elif running_config_confirmation == "no":
                                print_statement("Saved by the bullet, returning to main menu.")
                                os.system("clear")
                                time.sleep(2)
                                loop = 1


                            else:
                                print_statement("You have not entered a compatible command, please try again.")
                                system_exit()


                    elif help_command == 'show running':
                        print_statement("Type the IP address of the router you want to select.")
                        print("HQ Router: 192.168.1.1")
                        print("Bristol Router: 192.168.2.1")
                        print("Manc Router: 192.168.3.1")

                        yetanotherloop = str(input("Please select an IP: "))

                        if yetanotherloop == "192.168.1.1":
                            print_statement("Selected 192.168.1.1")


                        elif yetanotherloop == "192.168.2.1":
                            print_statement("Selected 192.168.2.1")


                        elif yetanotherloop == "192.168.3.1":
                            print_statement("Selected 192.168.3.1")


                        else:
                            print_statement("It appears you've entered the error IP address, please try again.")
                            system_exit()


                        B = yetanotherloop
                        get_router_ip(B)
                        print_statement("Please stand by, retrieving details. ")
                        time.sleep(2)
                        os.system("cat tmp.log")
                        print("\n")
                        running_config = str(input("(Wyvern):> yes/no Confirmation, Would you like to run the command Show run for this device?  "))

                        if running_config == "yes":
                            print("\n")
                            print(Fore.RED + "(Wyvern):> WARNING: Accepting will automatically run through a preset of commands on " '%s' % B + " device." + Style.RESET_ALL)
                            print("\n")


                        elif running_config == "no":
                            time.sleep(2)
                            system_exit()

                        running_config_confirmation = str(input(Fore.YELLOW + "(Wyvern):> yes/no Confirmation, Are you absolutely sure? " + Style.RESET_ALL))

                        if running_config_confirmation == "yes":
                            print_statement("Please stand by.")
                            time.sleep(2)
                            Show_running_config(B)
                            return

                        elif running_config_confirmation == "no":
                            print_statement("Saved by the bullet, returning to main menu.")
                            os.system("clear")
                            time.sleep(2)
                            loop = 1


                        else:
                            print_statement("You have not entered a compatible command, please try again.")
                            system_exit()


                except ValueError:
                    exception_trap()
                    return

            elif choice == 2:
                system_exit()


def paramiko_rip_config(M):  # Responsible for making the connection to the device.
    #Variables#
    ip = M

    #Admin credentials, these shouldn't change#
    username = 'admin'
    password = 'cisco'

    # create SSH object
    remote_ssh = paramiko.SSHClient()

    # add untrusted hosts to SSH
    remote_ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # SSH Connect
    remote_ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=True)
    print_statement("Connection established to %s " % ip)


    # Interactive Shell
    ssh_shell = remote_ssh.invoke_shell()
    print_statement("Secure SSH Connection Made.")


    # List of running commands
    ssh_shell.send("enable\n")
    ssh_shell.send("cisco\n") #password line
    ssh_shell.send("conf t\n")
    ssh_shell.send("router rip\n")
    ssh_shell.send("version 2\n")


    if M == "192.168.1.1":
        ssh_shell.send("network 172.16.3.1\n")
        ssh_shell.send("network 172.16.1.1\n")

    elif M == "192.168.2.1": #Bristol
        ssh_shell.send("network 172.16.1.2\n")
        ssh_shell.send("network 172.16.2.1\n")

    else: # Manchester
        ssh_shell.send("network 172.16.2.1\n")
        ssh_shell.send("network 172.16.3.1\n")


    ssh_shell.send("do show ip route\n")


    # Wait for command to complete
    time.sleep(5)
    # Receive Command outputs
    output = ssh_shell.recv(5000)
    file = output.strip()
    f = open('tmp.log', 'w')
    f.write(file.decode('utf-8'))
    f.write('\n')
    f.close()
    time.sleep(2)

    #Paramiko won't close the ssh socket automatically this takes care of that#
    ssh_shell.send("exit" + "\n")
    ssh_shell.close()

    print_statement("yes/no Confirmation, Would you like to view to output? ")
    Query = str(input("(Wyvern):>? "))


    if Query == 'yes':  # Display RIP output
        os.system('nano tmp.log')
        system_exit()

    elif Query == 'no':
        print_statement("Okay, exiting")
        time.sleep(2)
        system_exit()


    else:
        print_statement("Unknown quantifier, exiting")
        system_exit()


def paramiko_running_config(H):  # Responsible for making the connection to the device and gathering running config info.
    #Variables#
    ip = H
    #Admin credentials, these shouldn't change#
    username = 'admin'
    password = 'cisco'

    # create SSH object
    remote_ssh = paramiko.SSHClient()

    # add untrusted hosts to SSH
    remote_ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # SSH Connect
    remote_ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=True)
    print_statement("Connection established to %s " % ip)


    # Interactive Shell
    ssh_shell = remote_ssh.invoke_shell()
    print_statement("Secure SSH Connection Made.")


    # Commands
    ssh_shell.send("enable\n")
    ssh_shell.send("cisco\n")
    ssh_shell.send("terminal length 0\n") # Means the command doesn't have to tab.
    ssh_shell.send("show archive config diff\n")

    # Wait for command to complete
    time.sleep(8) # This command requires some time

    # Receive Command outputs
    output = ssh_shell.recv(5000)
    file = output.strip()
    f = open('tmp.log', 'w')
    f.write(file.decode('utf-8'))
    f.write('\n')
    f.close()

    time.sleep(5)
    #Paramiko won't close the ssh socket automatically this takes care of that#
    ssh_shell.send("exit" + "\n")
    ssh_shell.close()

    print_statement("yes/no Confirmation, Would you like to view to output? ")
    Query = str(input("(Wyvern):>? "))

    if Query == 'yes':  # Display RIP output
        os.system('nano tmp.log')
        system_exit()

    elif Query == 'no':
        print_statement("Okay, exiting")
        time.sleep(2)
        system_exit()

    else:
        print_statement("Unknown quantifier, exiting")
        system_exit()

def Show_running_config(B):  # Show running config function
    #Variables#
    ip = B
    #Admin credentials, these shouldn't change#
    username = 'admin'
    password = 'cisco'

    # create SSH object
    remote_ssh = paramiko.SSHClient()

    # add untrusted hosts to SSH
    remote_ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # SSH Connect
    remote_ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=True)
    print_statement("Connection established to %s " % ip)

    # Interactive Shell
    ssh_shell = remote_ssh.invoke_shell()
    print_statement("Secure SSH Connection Made.")

    # Commands
    ssh_shell.send("enable\n")
    ssh_shell.send("cisco\n")
    ssh_shell.send("terminal length 0\n") # Means the command doesn't have to tab.
    ssh_shell.send("Show run\n")
    # Wait for command to complete
    time.sleep(8)

    # Receive Command outputs#
    output = ssh_shell.recv(5000)
    file = output.strip()
    f = open('tmp.log', 'w')
    f.write(file.decode('utf-8'))
    f.write('\n')
    f.close()

    time.sleep(2)
    print_statement("Show archive config diff was outputted to the tmp.log")

    #Paramiko won't close the ssh socket automatically this takes care of that#
    ssh_shell.send("exit" + "\n")
    ssh_shell.close()
    print_statement("yes/no Confirmation, Would you like to view to output? ")
    Question2 = str(input("(Wyvern):>? "))

    if Question2 == 'yes': # Display comparison output
        os.system("diff -y tmp.log Offline_Local_RunConfig.txt") # Grep expression shows the differences between the two files.
        time.sleep(10)
        system_exit()

    elif Question2 == 'no':
        print_statement("Okay, exiting")
        time.sleep(2)
        system_exit()
    else:
        print_statement("Unknown quantifier, exiting")
        system_exit()


def print_statement(string):  # Responsible for newline handling with numerous print statements.
    print("\n" + Fore.YELLOW + "(Wyvern):> " + string + "\n" + Style.RESET_ALL)


def exception_trap():  # Responsible for handling unanticipated user input.
    print("\n")
    print("======================================================")
    print("Operation could not succeed. Error ", sys.exc_info()[0])
    print("======================================================")
    print("\n")
    time.sleep(3)


def get_router_ip(router_ip): # pings the device to make sure it's activity.
    os.system('ping ' + router_ip + ' -c 2 > tmp.log') #this automatically limits ping to 2 packets.


def wyvern_credits(): # Just credits for agent, author, license etc. Nonessential.
    print("\n")
    print("================================================")
    print("Wyvern: Python comparison agent | [Version]: 0.23")
    print("================================================")
    print(Fore.MAGENTA +'''        
     _    _                                  
    | |  | |                                 
    | |  | | _   _ __   __  ___  _ __  _ __  
    | |/\| || | | |\ \ / / / _ \| '__|| '_ \ 
    \  /\  /| |_| | \ V / |  __/| |   | | | |
     \/  \/  \__, |  \_/   \___||_|   |_| |_|
              __/ |                          
             |___/                           
            ''' + Style.RESET_ALL)
    print_statement(Fore.GREEN + "Created By Jake Madden")
    print_statement("I'll be damned if Wyvern isn't the little script that could!.")
    print_statement("It turns out if you do the thing and you do it right, it works, it just works!")
    print_statement("GNU General Public License v3.0 - Wyvern 2018" + Style.RESET_ALL)
    time.sleep(5)
    os.system("clear") # Linux sytax


def system_exit():
    print_statement("Thank you and goodbye Anon!")
    time.sleep(2)
    tmp_trap()
    os.system("clear")
    sys.exit()  # Raising system.exit means less memory usage after the application closes gracefully.


def tmp_trap(): # This does actually work providing the user doesn't use CRTL + Z while the script is running.
    #os.remove("tmp.log")
    exists = os.path.isfile('tmp.log')
	if exists:
    	os.remove("tmp.log")
	else:
    	print_statement("tmp.log doesn't exist, passing.")
    	pass


if __name__ == "__main__":
    app = WyvernAgent()
    app.main_menu_settings()
