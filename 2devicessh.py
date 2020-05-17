from netmiko import ConnectHandler

iosv_l2_SW5 = {
    'device_type' : 'cisco_ios',
    'ip' : '155.1.100.200',
    'username' : 'vivek',
    'password': 'vivek',
}

iosv_l2_SW6 = {
    'device_type' : 'cisco_ios',
    'ip' : '155.1.100.201',
    'username' : 'vivek',
    'password': 'vivek',
}

all_devices = [iosv_l2_SW5,iosv_l2_SW6]

for device in all_devices:
    print(f"logging to {device['ip']}")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip int br")
    net_connect.send_command("\n")
    print(output)
    for i in range(2 , 10):
        print(f"Creating vlan {i} ")
        commands = [f"vlan {i}" , f"name  AUTOMATION_VLAN_{i}"]
        output= net_connect.send_config_set(commands)
        net_connect.send_command("\n")
        print(output)
    output1 = net_connect.send_command("wr mem")
    print(output1)

