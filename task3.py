import re
import os
from ping3 import ping, verbose_ping

def valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip)

def ping_ip(ip):
    try:
        result=ping(ip)
        return result
    except Exception as e:
        print(f"An error occured: {e}")
        return False
def add_ip():
    ip_put=input("Enter ip address : ")
    if valid_ip(ip_put):
        print("Valid ip")
        if ping_ip(ip_put):
            with open("pinging.txt","a") as file:
                file.write(ip_put + "\n")
            print("ping successful")
        else:
            with open("not_pinging.txt","a") as file:
                file.write(ip_put + "\n")
            print("ping unsuccessful")
    else:
        print("Invalid IP")

    choose = input("Do you want validate ips ?(yes or no): ")
    if choose.lower()== 'yes':
        add_ip()
    else:
        print("OK, Thank You")
def print_ips (f_name):
    ips=[]
    with open(f_name,"r") as file:
       ips=file.readlines()
    return ips
add_ip()

pinged_ip=print_ips("pinging.txt")
not_pinged_ip=print_ips("not_pinging.txt")
print("PINGED IP's ARE:\n")
for ip in pinged_ip:
    print("->",ip)
print("NOT PINGED IP's ARE:\n")
for ip in not_pinged_ip:
    print("->",ip)

os.remove("pinging.txt")
os.remove("not_pinging.txt")
    
