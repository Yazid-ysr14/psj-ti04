import os
import sys
import concurrent.futures

def check(data):
    for x in data :
        c_host = os.system('ping -c3 '+x+' >/dev/null 2>&1')
        if(c_host == 0):
            print("Host " + x + " is UP")
        else:
            print("Host " + x + " is DOWN")

    return "proses selesai"

with concurrent.futures.ProcessPoolExecutor() as executor:
    hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4'] 

    results = [executor.submit(check,hosts) for _ in range(1)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
