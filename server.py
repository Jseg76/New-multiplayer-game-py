import socket as s
import pickle
import threading as t

host = s.gethostbyname(s.gethostname())
port = 8000

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
print(f'Server listening on {host}')

clients = []

def handle_client(conn):
    clients.append(conn)
    print('client connected')
    while True:
        try:
            data = pickle.loads(conn.recv(1024))
        except:
            conn.close()
            clients.remove(conn)
            print('client disconnected')
            break


while True:
    conn, addr = server.accept()
    t.Thread(target=handle_client, args=(conn,)).start()