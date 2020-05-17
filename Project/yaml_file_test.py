
"""Importing the YAML FILE
This script will check the yaml file with dict

""" 
import yaml

#Reading the YAML file 

def read_yaml_file(path='Invetory_FILE/Host_YMAL_FILE.yml'):
	with open(path)  as f:
		#load the data safe with function
	#parses the given stream and returns a Python object constructed from for the first document in the stream. If there are no documents in the stream, it returns None.
		yaml_content = yaml.safe_load(f.read())
	return  yaml_content



def main():
	parse_output = read_yaml_file()
	print(parse_output)

if __name__ == "__main__":
	main()
