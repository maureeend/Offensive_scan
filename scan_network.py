import platform
import socket
import os
import subprocess

# Print OS
print(platform.system())

# find localhost 
localhost = socket.gethostname()

# Add Ipconfig in file
with open('ip_info.txt', 'w') as fl:
    ip_info = subprocess.run(['ipconfig'],stdout=fl)
    fl.close()

# Create a file with an ip
with open('ip_info.txt','r') as fl:
    ip_info = fl.read()
    
    for line in ip_info.split('\n'):

        if 'IPv4' in line:
            ip_address = line.split(':')[-1].strip()
            print(ip_address)

            with open('info_adresse.txt', 'w') as fm:
                fm.write(str(ip_address))
                fm.close()
            
    fl.close()


with open('info_adresse.txt', 'r') as fn:
    info_adresse = fn.read()
    ip = info_adresse.strip()
    partial_ip = '.'.join(ip.split('.')[:3])
    print("--")
    print(partial_ip)

    fn.close()

    for i in range(0, 3):
        target = f"{partial_ip}.{i}"
        response = subprocess.run(['ping', '-n', '1', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Vérifier si le ping a réussi
        if response.returncode == 0:
            print(f"Succès : {target} est accessible")
        else:
            print(f"Échec : {target} n'est pas accessible")



