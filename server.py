import socket
import threading


ip_address = '192.168.0.23'
port = 5075

def handle_client(connection,address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        command = input('cmd>> ')
        if command.lower() in ['exit','quit','q','x']:    
          break
 
        connection.send(command.encode())
        host_and_key = connection.recv(1024).decode()
          #print(f"Message from client is :{host_and_key}")
        received = f"Data received:{host_and_key}"
        print(received)
    connection.close()
        
        
def main():
      
    print("Welcome on Server")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind((ip_address, port))
        print("Listening ...|/*\|..|/*\|")
        soc.listen(5)

        while True:
            
            connection, address = soc.accept()
            connection.send('conneted'.encode())
            thread = threading.Thread(target=handle_client, args=(connection,address))
            thread.start()
            print(f"[ACTIVE CONNECTTION] {threading.active_count() -1}")
            print(f"Connection from {address} established!")
            # deepcode ignore single~iteration~loop: <please specify a reason of ignoring this>
            

if __name__ == "__main__":
    main()
