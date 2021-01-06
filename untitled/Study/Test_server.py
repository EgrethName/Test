import socket
import threading


def client(conn_c):
    while True:
        data = conn_c.recv(1024)
        if data == 'close':
            break
        conn_c.send(data)
    conn.close()


s = socket.socket()
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=client, args=(conn, ))
    t.start()
