import socket as s
import pickle
import threading as t
from player import Player

host = s.gethostbyname(s.gethostname())
port = 8000

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
print(f'Server listening on {host}')

clients = []
playerData = []
clientNum = 0

def handle_client(conn, num):
    global clientNum
    clients.append(conn)
    playerData.append(num)
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            playerData[num] = data
            conn.send(pickle.dumps(playerData))
            print(playerData)
        except:
            clientNum -= 1
            conn.close()
            clients.remove(conn)
            print('client disconnected')
            break

while True:
    conn, addr = server.accept()
    t.Thread(target=handle_client, args=(conn, clientNum)).start()
    clientNum += 1