from netmiko  import ConnectHandler
from datetime import datetime
from copy import deepcopy
import yaml
import time


""" 
	Getting the Host file from our yaml file that has all the list  host in the network 

""" 



def host_yaml(path="Invetory_FILE/Host_YMAL_FILE.yml"):
	with open(path) as f:
		yaml_content = yaml.safe_load(f.read())
	return yaml_content

"""
		 Getting the Host file from our yaml file that has all the list  commands which need in the network

"""

def command_yaml(path= "Invetory_FILE/command_line.yml"):
	with open(path) as f:
		command = yaml.safe_load(f.read())
	return command
### Combining the both varible in  the HOST Invetory file 
### Which has  both username and host 
 


def get_connection_parameter(parsed_yaml):
	
	parsed_yaml = deepcopy(parsed_yaml)
	#Getting the Username and Passwords
	login_credentials = parsed_yaml["vars"]
	# Combining the UserName and Passwords with each host for netmiko ConnectHandler
	for host in parsed_yaml["hosts"]:
		host_dict = {}
		host_dict.update(login_credentials)
		host_dict.update(host)
	"""	The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. 
		When resumed, the function continues execution immediately after the last yield run.
		 This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
	"""
		yield host_dict
### Putting show  commands into the decive and setting connection


def show_commands(devices , commands):
	for device in devices:
		if device['host'] ==  
		start_time =datetime.now()
		hostname =device['host']
		connection = ConnectHandler(**device)
		device_result= ["{0} {1} {0}".format("="*10,hostname)]	
		for command in commands:
			command_result = connection.send_command(command)
			device_result.append("{0} {1} {0}".format("=" * 10, command))
			device_result.append(command_result)
		device_result_string = "\n\n".join(device_result)
		connection.disconnect()
		device_result_string += "\nElapsed time:" + str(datetime.now() - start_time)
		yield device_result_string



def main():
	COMMANDS = command_yaml()
	show_command = (COMMANDS['command'])
	print(show_command)
	parse_output =  host_yaml()
	print(parse_output)
	
	connection_parameters =  get_connection_parameter(parse_output)
	print(f"=============={type(connection_parameters)}===========")
	for device_result in show_commands(connection_parameters,show_command):
		print(device_result)

#Calling the Main Function
if __name__ == "__main__":
	main()
