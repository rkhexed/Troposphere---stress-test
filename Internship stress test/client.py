import socket
import json
import time
import threading
import Stress_test as s2
HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    s.sendall(b"Initiating ping system")
    data = s.recv(1024)


print(f"Received {data!r}")
my_json = data.decode('utf8').replace("'", '"')

data = json.loads(my_json)
ss = json.dumps(data, indent=4, sort_keys=True)
print(data)


def ping_system():
    status = {"alive":"true"}
    nostatus =  {"alive":"false"}
    status = json.dumps(status)
    nostatus = json.dumps(nostatus)
    count=0
    a=1
    while a == 1:    
        if count%5==0:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(b'alive:true')
        if count >  data['max_time_seconds']:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(b'alive:false')
            break
        count += 1
        time.sleep(1)

t1 = threading.Thread(target=ping_system,args=())
t1.start()

s2.DEFAULT_TIME=data['max_time_seconds']
s2.TOTAL_CPU=data['CPU_percent']
s2.DEFAULT_MEMORY=data['Memory_percent']
s2._main()




    




    
