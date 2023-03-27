import socket
import hashlib
import rsa

HOST = '127.0.0.1'
PORT = 7791

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('receiving public key...')
    with open('server_public', 'wb') as server_pub:
        server_pub.write(s.recv(1024))

    print('sending public key...')
    with open('client_public', 'rb') as key:
        s.send(key.read())
    
    plaintxt = input('> ').encode()
    hash = hashlib.sha256(plaintxt).digest()
    sig = rsa.encrypt(hash, 'client_private')
    ciphertxt = rsa.encrypt(plaintxt, 'server_public')
    s.sendall(sig + ciphertxt)
    
    data = s.recv(1024).decode()

print(data)