#! /bin/bash
#Script to Select Python File to Run


#Defining File Locations
hq = /root/OSPF/hq_ospf.py
bristol = /root/OSPF/bristol_ospf.py
manchester = /root/OSPF/manchester_ospf.py
ssh = /root/ssh.py
telnet = /root/telnet.py
retrieve_info = /root/fetch_info.py
rip-compare_config = /root/Wyvern/wyvern.py

#Show Options
echo "-------------------------------------------------------------"
echo "This is Python Network Automation"
echo "Choose one of the options below to continue..."
printf '\n'

echo "1. Establish Telnet Connection to Device"
echo "2. Establish SSH Connection to Device"
echo "3. Configure OSPF"
echo "4. Configure RIP and Compare Configuration Information"
echo "5. Fetch Device Information"

#INPUT
echo "Please enter your choice below:"
read option 

#Telnet
if [$option == "1"] 
then
	/usr/bin/python telnet

#SSH
elif [$option == "2"]
then 
	/usr/bin/python ssh

#OSPF
elif [$option == "3"]
then 
	echo "Choose which Router you are configuring..."
	printf '\n'
	
	echo "1. HQ Router"
	echo "2. Bristol Router"
	echo "3. Manchester Router"
	
	echo "Please enter your choice below:"
	read router
	
	#HQ
	if [$router == "1"]
	then
		/usr/bin/python hq
		
	#Bristol
	elif [$router == "2"]
	then 
		/usr/bin/python bristol
		
	#Manchester
	elif [$router == "3"]
	then 
		/usr/bin/python manchester
		
	fi 


#RIP and Compare Configuration
elif [$option == "4"]
then
	/usr/bin/python rip-compare_config
	
#Fetch Configuration
elif [$option == "5"]
then
	/usr/bin/python retrieve_info
	
fi 