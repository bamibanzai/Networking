import pexpect

#establishing the connection
ip_address = raw_input("What IP address do you want to connect to? \n")

username = raw_input("What is the Username? \n")
password = raw_input("What is the Password? \n")

#creating pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout = 10)
result = session.expect(['Username:', pexpect.TIMEOUT])


if result != 0:
    print '--- FAILURE! creating session for: ', ip_address
    exit()

session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! entering username: ', username
    exit()

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' FAILURE! entering password: ', password
    exit()	


print "\nSuccess connecting to: ", ip_address
print "\nBelow is the telnet session"


session.sendline ("\n")
session.sendline ("enable")
session.sendline ("cisco") 
session.sendline ("wr")

#Makes the session interactable
session.interact()
