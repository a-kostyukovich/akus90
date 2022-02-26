import sys, time, csv, os
from old_gen_class_daemon import Daemon
 
class MyDaemon(Daemon):
        def run(self):
                while True:
                        time.sleep(60)
                        with open('/proc/net/arp') as arp_table:
    	                #'IP address', 'HW type', 'Flags', 'HW address', 'Mask', 'Device'
                                spamreader = csv.reader(arp_table, skipinitialspace=True, delimiter=' ')
                                for row in spamreader:
                                    if row[5] == 'eth0':
                                        print(row[0] + ' ' + row[3] + ' ' + row[5])
 
if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print('Unknown command')
                        sys.exit(2)
                sys.exit(0)
        else:
                print("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)