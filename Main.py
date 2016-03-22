import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)

dataSize = 1024

clients = []

while True:
    conn, addr = sock.accept()
    conn.setblocking(0)
    clients.append(conn)
    
    for client in clients:    
        data = client.recv(dataSize)
        if not data:
            continue

        if data == "close":
            client.close()
            clients.remove(client)
            continue
        
        client.send(data)