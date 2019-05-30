import os #For running scripts


#Show Options
print "-------------------------------------------------------------"
print "This is Python Network Automation"
print "Choose one of the options below to continue...\n"

print "1. Establish Telnet Connection to Device"
print "2. Establish SSH Connection to Device"
print "3. Configure OSPF"
print "4. Configure RIP and Compare Configuration Information"
print "5. Fetch Device Information"

option = raw_input("Please enter your choice:")

if option == "1":
	print "Running telnet script..."
	os.system('python telnet.py')
elif option == "2":
	print "Running ssh script..."
	os.system('python ssh.py')
elif option == "3": 
	print "Choose which Router you are configuring..."
	
	print "1. HQ Router"
	print "2. Bristol Router"
	print "3. Manchester Router"
	
	router = raw_input("Please enter your choice:")
	
	if router == "1":
		print "Configuring HQ OSPF..."
		os.system('python hq_ospf.py')
	elif router == "2":
		print "Configuring Bristol OSPF..."
		os.system('python bristol_ospf.py')
	elif router == 3:
		print "Configuring Bristol OSPF..."
		os.system('python manchester_ospf.py')

elif option == "4":
	print "Opening RIP and Compare Configuration..."
	os.system('python wyvern.py')
elif option == "5":
	print "Preparing to fetch device info.."
	os.system('python fetch_info.py')
