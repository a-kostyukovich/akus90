import daemon, sys

from new_gen_do_it import do_it_now

with daemon.DaemonContext(stdout=sys.stdout):
    do_it_now()