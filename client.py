 import socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 8080))
    client.send("I am Evitas CLIENT<br>")
    from_server = client.recv(3333)
    client.close()
    print from_server
