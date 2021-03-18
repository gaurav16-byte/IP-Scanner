import sys
import subprocess as s

def specific():
    ips = input('Enter the specific IP Addresses you want to scan separated by a space ').split()
    for i in ips:
        a = s.run(['ping', i], capture_output=True, text=True).stdout
        if 'Destination host unreachable' not in a:
            print('The IP ',i,' is on the network')
        else:
            print('The IP ',i,' is not on the network')

def over_range():
    ips = input('Enter IPS with the starting and the end point, Ex. 192.168.1.1 192.168.1.20')
    ips_list = ips.split()
    end_range = ips_list[-1].rfind('.')
    last = ips_list[-1][end_range + 1:]
    begin_range = ips_list[0].rfind('.')
    begin = ips_list[0][begin_range + 1:]
    for i in range(int(begin),int(last) + 1):
        a = s.run(['ping',ips_list[0][:ips_list[0].rfind(begin)] + str(i)], capture_output=True, text=True).stdout
        if 'Destination host unreachable' not in a:
            print('The device with the IP ',ips_list[0][:ips_list[0].rfind(begin)] + str(i),' is available on the network')
        else:
            print('The device with the IP ',ips_list[0][:ips_list[0].rfind(begin)] + str(i),' is not available on the network')

def one_ip():
    ip = input('Enter your ip ')
    a = s.run(['ping', ip], capture_output=True, text=True).stdout
    if 'Destination host unreachable' not in a:
        print('A device with the IP ',ip,' is available on the network')
    else:
        print('A device with the IP ',ip,' is not available on the network')

print('A)SCAN A SINGLE IP')
print('B)SCAN SPECIFIC IPS')
print('C)SCAN IPS OVER A RANGE OF IPS EX.192.268.2.1-24')
print('D)EXIT')
while True:
    choice = input('Enter your choice ')
    while choice not in 'ABCDabcd':
        print('Invalid Choice')
    else:
        if choice in 'Aa':
            one_ip()
        elif choice in 'Bb':
            specific()
        elif choice in 'Cc':
            over_range()
        elif choice in 'Dd':
            sys.exit()
