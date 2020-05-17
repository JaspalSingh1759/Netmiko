from netmiko import ConnectHandler
from getpass import getpass

R1 = {
    'host': 'R1',
    "username": "vivek",
    "password": getpass(),
    "device_type": "cisco_ios",
}

connection = ConnectHandler(**R1)
print(connection.find_prompt())
connection.disconnect()
