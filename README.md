# TCPBeast
A python program that optimizes the traffic analysis capabilities for Wireshark and tcpdump via linux.

This repository will contain the following: Code for the optomization of the wireshark outputs, and an explanation of how it works & how you may further optomize this for yourself.

There is no licensing, copyrights, etc involved. Feel free to use and reproduce this however you wish!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To fully set this up from scratch, you will first need to install wireshark. You should first update your installer via the apt update command, and then use apt install wireshark to complete the installation. 

Once wireshark is downloaded, you can download tshark utilizing almost the same command, apt install tshark.

From there, it is time to perform our first packet capture via tcpdump. The first thing we will need to do is find our host IP address. Most linux packages will come with networking tools pre-installed. 

To view your networking interfaces, utilize the command ifconfig. This will bring up a list of your available interfaces. If you are using an ethernet connection, your default interface should be eth0. 

If you are unsure of what interface you are using, an easy way to find this is to stream a video, such as youtube or netflex, and run the command. The interface with the most packets is likely to be your main interface.

Once you find your interface, we may begin the packet capture via tcpdump. To do this, simply input the following into your command line: tcpdump -i (your interface here) -vv ip host (your ip here) -w traffic.pcap

This command will run the packet capture on the interface and ip address inputed, and write the output to a new file called traffic.pcap . My command looks like this: tcpdump -i eth0 -vv ip host 192.168.0.1 -w traffic.pcap

Once you submit the command, your packet capture will be running. Head over to an HTTP website and play around with it! If there is an option to attempt a login with a username and password, that will be excellent. When you are ready to move on, simply head back to your command line and use control+c to end the packet capture. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the capture is completed, it is time do utilize the script to view a nice, neat version of the packet capture. We do need to modify a few things first.

To start, we will need to change the permissions of the traffic.pcap file as well as create the tcpbeast python script. 

Go ahead and create a new text file with the default editor nano, usng the command nano tcpbeast.py (or whatever you'd like to name it, as long as it ends with .py!). Once you've copied in the script, use control+x to save and name the file appropriately. 

Once the file is saved, we can then change the permissions. Use command chmod 777 tcpbeast.py (or whatever you've named it) to ensure that the execution is available for this script. 

To make life easier, you can use the same command for the traffic output file, traffic.pcap : chmod 777 traffic.pcap

Now that everything is ready, it is time to run the script! Simply input ./tcpbeast.py (or whatever you've named it) followed by the name of the traffc file. Following our example, the command would look like: ./tcpbeast.py traffic.pcap

Once the script is done running, it will have created a new text file called trafficstreams.txt (or whatever you named the pcap file) into the same directory. To view this, simply input the command ls to show the available documents in the directory. 

Once you find the new document, you may view it with the cat command : cat trafficstreams.txt

That's all for this one!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
