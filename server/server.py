import socket
# import jks
import hashlib
import rsa
import threading

def thread_task(client, address):
    print(f'connection from {address}')

    print('sending public key...')
    with open('server_public', 'rb') as key:
        client.sendall(key.read())

    print('receiving public key...')
    with open('client_public', 'wb') as key:
        key.write(client.recv(1024))

    sigmsg = client.recv(1024)
    sig = sigmsg[:64]
    ciphertxt = sigmsg[64:]
    sent_hash = rsa.decrypt(sig, 'client_public')
    plaintxt = rsa.decrypt(ciphertxt, 'server_private')
    local_hash = hashlib.sha256(plaintxt).digest()

    if local_hash.hex() == sent_hash.hex():
        print('Message Verified!')
        print(plaintxt.decode())
    else:
        print('Invalid digital signature, discarding message.')
        
    return
                
# keystore = jks.KeyStore.new('jks', [])
# keystore.save('server.jks', 'password1234')

HOST = '127.0.0.1'
PORT = 7791

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        client, address = s.accept()
        threading.Thread(target=thread_task, args=(client, address)).start()
        