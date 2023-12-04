
# importing os module
import os
import socket
import requests
 
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address
 
# Call the function to get the IP address
ip = get_ip_address()
print("IP Address:", ip)


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)
 
# using getlogin() returning username
print(os.getlogin())


