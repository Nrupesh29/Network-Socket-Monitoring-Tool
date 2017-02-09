"""
CMPE 273 - Enterprise Distributed Systems
Python Version: 2.7.12
Platform: MacOS
Student ID: 011425271
"""

from collections import OrderedDict
import psutil

PROCESSES = {}

print "\"pid\",\"laddr\",\"raddr\",\"status\""

for c in psutil.net_connections(kind='tcp'):
    if c.laddr and c.raddr:
        if c.pid in PROCESSES:
            PROCESSES[c.pid].append("\"" + str(c.pid) + "\",\"" + str(c.laddr[0]) + "@" 
                    + str(c.laddr[1]) + "\",\"" + str(c.raddr[0]) + "@" + str(c.raddr[1]) + "\",\"" + c.status + "\"")
        else:
            PROCESSES[c.pid] = ["\"" + str(c.pid) + "\",\"" + str(c.laddr[0]) + "@" 
                    + str(c.laddr[1]) + "\",\"" + str(c.raddr[0]) + "@" + str(c.raddr[1]) + "\",\"" + c.status + "\""]

SORTED_PROCESSES = OrderedDict(sorted(PROCESSES.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))

for k, v in SORTED_PROCESSES.items():
    for i in v:
        print (i)