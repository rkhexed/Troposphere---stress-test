import socket
import json

HOST = "127.0.0.1"  
PORT = 65432 
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                print('received data ',data)
                if not data:
                    break
                else:
                    f=open('stressdata.json','r') # insert config file name, within same folder
                    data=json.load(f)
                    '''
                    print(type(data))
                    print(data)
                    '''
                    jsonResult = json.dumps(data)
                    arr = bytes(jsonResult, 'utf-8')
                    conn.sendall(arr)
                    break


                    

                     
                    