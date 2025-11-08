import sys
import requests
import socket 
from pyfiglet import Figlet

choice = Figlet(font='slant')
print()
print(choice.renderText("IP AGENT"))
print()

class IPAGENT():
    def __init__(self, ip):  
        self.ip = ip
        self.response = ""
        self.data = {}
    def getlocation(self):
        try:
            self.response = requests.get(url=f'http://ip-api.com/json/{self.ip}').json()
            self.data['[IP]'] = self.response.get('query')
            self.data['[Int prov]'] = self.response.get('isp')
            self.data['[Country]'] = self.response.get('country')
            self.data['[Country code]'] = self.response.get('countryCode')
            self.data['[ZIP]'] = self.response.get('zip')
            self.data['[LAT]'] = self.response.get('lat')
            self.data['[LON]'] = self.response.get('lon')
        except requests.exceptions.ConnectionError:
            print('[!] Connection failure!')
    def show(self):         
        for k in self.data:
            print(f'{k} : {self.data[k]}')


ip = input("Please input an ip address ")
ip1 = IPAGENT(ip)

ip1.getlocation()
ip1.show()