from netmiko  import ConnectHandler
from datetime import datetime
from copy import deepcopy
import yaml
import time

COMMANDS = [ 
	"show ip route " , "show ip int br | ex admin"
	]

def read_yaml(path="Invetory_FILE/Host_YMAL_FILE.yml"):
	with open(path) as f:
		yaml_content = yaml.safe_load(f.read())
	return yaml_content

def get_connection_parameter(parsed_yaml):
	parsed_yaml = deepcopy(parsed_yaml)
	login_credentials = parsed_yaml["vars"]
	for host in parsed_yaml["hosts"]:
		host_dict = {}
		host_dict.update(login_credentials)
		host_dict.update(host)
		yield host_dict
		#print(host_dict)
def show_commands(devices , commands):
	for device in devices:
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
	parse_output =  read_yaml()
	print(parse_output)
	connection_parameters =  get_connection_parameter(parse_output)
	print(f"=============={type(connection_parameters)}===========")
	for device_result in show_commands(connection_parameters,COMMANDS ):
		print(device_result)
if __name__ == "__main__":
	main()
