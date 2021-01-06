import socket
import threading

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)


def run_recv(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('received: {}'.format(data.decode()))


recv_thread = threading.Thread(target=run_recv, args=(conn, ))
recv_thread.start()

while True:
    data = input("Type your message: > ")
    conn.send(data.encode())


recv_thread.join()
conn.close()
