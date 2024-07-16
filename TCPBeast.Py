#!/usr/bin/python3
import sys
from subprocess import PIPE, Popen

def cmdline(command): #Defines our function to run a command in the shell and capture its output
	process = Popen(args=command, stdout=PIPE, shell=True, universal_newlines=True)
	return process.communicate()[0]

def filter_stream(stream): #Defines our function to filter lines from the stream based on various conditions
	filtered_lines = []
	inside_random_section = False

	lines = stream.splitlines() #Splits the stream into individual lines
	ignore_starts = set('0123456789!@#$%^&*()-_+{[}],<>?/|~`') #Defines our rule for filtering out any lines of output text that start with any of these characters
	ignore_strips = set('abcdefghijklmnopqrstuvwxyz') #Defines our rule for filtering out any lines of output text that contain only a single alphabetical character
	for i, line in enumerate(lines): #Begins the check for un-necessary output text.
		if '..' in line:
			inside_random_section = True
		if '..' in line and inside_random_section:
			inside_random_section = False
			continue
		if line.startswith(tuple(ignore_starts)) or line.strip() in ignore_strips: #Continues checking for un-necessary output text via the two earlier definitions
			continue
		if line.strip() == '' and (i == 0 or lines [i - 1] != '=============================='): #Ensures proper spacing and new line return once the stream is done
			continue
		if 1 <= len(line.strip()) < 9: #Removes any lines with less than 9 characters
			continue
		if not inside_random_section: # Adds output lines to filtered_lines if not containing unnecessary information.
			filtered_lines.append(line)

	return '\n'.join(filtered_lines)

pcap_file = sys.argv[1] #Fetches the pcap file name from the command-line arguments
output_file_name = pcap_file.split('.')[0] + 'streams.txt' #Creates the output file name based on the input file name
output_file = open(output_file_name, 'w') #Opens the output file for writing
count = 0
while True:     #Creates a command to run tshark on the pcap file and follow TCP streams.
	cmd = 'tshark -r %s -z follow,tcp,ascii,%s' %(pcap_file,count) 
	stream = cmdline(cmd)  #Runs the command and captures the output.
	if '===================================================================' in stream: #Processes the stream if it contains the separator line.
		stream = stream.split('===================================================================\n')[1]
		stream += '\n\n==============================\n\n'
	filtered_stream = filter_stream(stream) #Filters the stream to remove unwanted lines.
	if 'Node 0: :0' not in filtered_stream: #Write the filtered stream to the output file if it doesn't contain 'Node 0: :0', which indicates there is no more traffic to analyze. This prevents an endless loop.
		output_file.write(filtered_stream)
	else:
		break
	count += 1
output_file.close() #Closes the output file.
