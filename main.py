import requests
from  colorama import init,Fore,Back

init()

response = requests.get('https://httpbin.org/ip')

print(Back.BLUE + Fore.YELLOW +'Your IP is {0}'.format(response.json()['origin']))