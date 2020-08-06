#!/usr/bin/env python3
import netifaces

# Customization 1 & 2

# print only MAC addresses
print(netifaces.interfaces())
def main():
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC: ', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        except:
            print('Could not collect adapter info')
main()
# print only IP addresses
print(netifaces.interfaces())
def main():
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('IP: ', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
        except:
            print('Could not collect adapter info')
main()
