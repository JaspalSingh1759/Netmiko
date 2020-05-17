import yaml

def lists_yaml(path="command_line.yml"):
	with open(path) as f:
		ymal_content = yaml.safe_load(f.read())
	return ymal_content

def main():
	parse_output =  lists_yaml()
	print(parse_output)
	command= (parse_output['command'])
	print(command[1])
	
if __name__  == "__main__":
	main()
