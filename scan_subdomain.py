import sys
import requests

# lecture fichier
with open("subdomains-top1million-5000.txt") as fl:
    subdom = [line.rstrip("\n") for line in fl]

if len(sys.argv) < 2:
    sys.exit(1)

domain = sys.argv[1]

for sub in subdom:
    sub_domain = f"https://{sub}.{domain}"
    
    try:
        requests.get(sub_domain)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domain)
