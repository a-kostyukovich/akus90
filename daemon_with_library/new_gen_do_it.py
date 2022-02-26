import sys, os, time, csv

def do_it_now():
    while True:
        time.sleep(60)
        with open('/proc/net/arp') as arp_table:
        #'IP address', 'HW type', 'Flags', 'HW address', 'Mask', 'Device'
            spamreader = csv.reader(arp_table, skipinitialspace=True, delimiter=' ')
            for row in spamreader:
                if row[5] == 'eth0':
                    print(row[0] + ' ' + row[3] + ' ' + row[5])