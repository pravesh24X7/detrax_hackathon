#!/usr/bin/env python3

import os
import subprocess as sb
import re
import socket


def find_posix_active_connections():

    result = str(sb.check_output('netstat -natp', shell=True))
    ip_addresses = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,3}", result)

    return ip_addresses



def system_connections():

    if os.name == 'posix':
        return find_posix_active_connections()
    else:
        return find_ntos_active_connections()


def main():
    
    ip_addresses = system_connections()
    for ip in ip_addresses:
        addr, port = ip.split(':')
        print('[+] IP: {} Connected To PORT: {}'.format(addr, port))

    acon = []
'''
    # code to check active connections 
    for ip in ip_addresses:
        addr, port = ip.split(':')
        
        try:
            acon.append(socket.create_connection((addr, port), timeout=1))
        except OSError:
            pass
    print(acon)
'''

if __name__ == '__main__':
    main()
