from socket import socket , AF_INET , SOCK_STREAM
import os

def send(path_file):
    soc = socket(AF_INET,SOCK_STREAM)
    soc.settimeout(3)
    buffer_size = 1 * 1024 * 1024 # 1 MB
    sent = 0
    file_name = os.path.basename(path_file)
    file_size = os.path.getsize(path_file)
    soc.connect(("192.168.43.1",4444))
    soc.sendall(f"{file_name}§{file_size}§".encode())
    with open(path_file,"rb") as f:
        while True:
            buffer = f.read(buffer_size)
            if not buffer:
                break
            soc.sendall(buffer)
            sent += len(buffer)
            percent = (sent/file_size) * 100
            if int(percent) % 5 == 0:
                print(f"\rFile sent : {int(percent)} %",end="",flush=True)
        print("\n[+] File has been sent")
        soc.close()
#-----------------------#-------------------------#
def receive():
    soc = socket(AF_INET,SOCK_STREAM)
    received = 0
    buffer_size = 1 * 1024 * 1024 # 1 MB
    soc.bind(("0.0.0.0",4444))
    soc.listen(1)
    print("Listening started in 4444")
    client , addr = soc.accept()
    print(f"Connected with {addr}")
    meta_data = client.recv(1024).split("§".encode("utf-8"))
    file_name = meta_data[0].decode()
    file_size = int(meta_data[1].decode())
    os.makedirs("/sdcard/SharePY",exist_ok=True)
    print(f"File Size : {round(file_size/1024/1024,2)} MB")
    with open(f"/sdcard/SharePY/{file_name}","wb") as f:
        if meta_data[2]:
            f.write(meta_data[2])
            received += len(meta_data[2])
        while True:
            buffer = client.recv(buffer_size)
            if not buffer:
                break
            f.write(buffer)
            received += len(buffer)
            percent = (received/file_size) * 100
            if (int(percent)) % 5 == 0:
                print(f"\rFile received : {int(percent)} %",end="",flush=True)
        print(f"\n[+] File saved in /sdcard/SharePY/{file_name}")
        client.close()
        soc.close()
#-----------------------#-------------------------#
try:
    x = int(input("1- send\n2- receive\nEnter Num : "))
except ValueError as e:
    print(f"Error-Choose: {e}")

if x == 1:
    print("[*] You must open WiFi and connect with HotSpot.")
    p = input("Enter Path file : ")
    try:
        send(p)
    except ConnectionError as e:
        print(f"Error-Connection: {e}")

elif x == 2:
    print("[*] You must open HotSpot")
    receive()
