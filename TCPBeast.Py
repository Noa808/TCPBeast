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
	for i, line in enumerate(lines): #Begins the check for un-necessary output text.
		if '..' in line:
			inside_random_section = True
		if '..' in line and inside_random_section:
			inside_random_section = False
			continue
		if line.startswith('.'):
			continue
		if line.startswith('@'):
			continue
		if line.startswith('#'):
			continue
		if line.startswith('$'):
			continue
		if line.startswith('%'):
			continue
		if line.startswith('^'):
			continue
		if line.startswith('&'):
			continue
		if line.startswith('*'):
			continue
		if line.startswith('('):
			continue
		if line.startswith(')'):
			continue
		if line.startswith('_'):
			continue
		if line.startswith('-'):
			continue
		if line.startswith('+'):
			continue
		if line.startswith('~'):
			continue
		if line.startswith('`'):
			continue
		if line.startswith('!'):			
			continue
		if line.startswith('{'):
			continue
		if line.startswith('}'):
			continue
		if line.startswith('['):
			continue
		if line.startswith(']'):
			continue
		if line.startswith('|'):
			continue
		if line.startswith('<'):
			continue
		if line.startswith('>'):
			continue
		if line.startswith('?'):
			continue
		if line.startswith(','):
			continue
		if line.startswith('/'):
			continue
		if line.startswith('1'):
			continue
		if line.startswith('2'):
			continue
		if line.startswith('3'):
			continue
		if line.startswith('4'):
			continue
		if line.startswith('5'):
			continue
		if line.startswith('6'):
			continue
		if line.startswith('7'):
			continue
		if line.startswith('8'):
			continue
		if line.startswith('9'):
			continue
		if line.strip() == '1400':
			continue
		if line.strip() == 'a':
			continue
		if line.strip() == 'b':
			continue
		if line.strip() == 'c':
			continue
		if line.strip() == 'd':
			continue
		if line.strip() == 'e':
			continue
		if line.strip() == 'f':
			continue
		if line.strip() == 'g':
			continue
		if line.strip() == 'h':
			continue
		if line.strip() == 'i':
			continue
		if line.strip() == 'j':
			continue
		if line.strip() == 'k':
			continue
		if line.strip() == 'l':
			continue
		if line.strip() == 'm':
			continue
		if line.strip() == 'n':
			continue
		if line.strip() == 'o':
			continue
		if line.strip() == 'p':
			continue
		if line.strip() == 'q':
			continue
		if line.strip() == 'r':
			continue
		if line.strip() == 's':
			continue
		if line.strip() == 't':
			continue
		if line.strip() == 'u':
			continue
		if line.strip() == 'v':
			continue
		if line.strip() == 'w':
			continue
		if line.strip() == 'x':
			continue
		if line.strip() == 'y':
			continue
		if line.strip() == 'z':
			continue
		if line.strip() == '' and (i == 0 or lines [i - 1] != '=============================='):
			continue
		if 1 <= len(line.strip()) < 9:
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
