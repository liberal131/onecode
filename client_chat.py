import socket

def main():
    host = '127.0.0.1'
    port = 12346
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        print("Type 'bye' to exit the chat")
        print("=" * 50)
        
        while True:
            message = input("You: ")
            
            if message.lower() == 'bye':
                client_socket.send(message.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print(f"Server: {response}")
                break
            
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {response}")
            
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Is the server running?")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("\nConnection closed")

if __name__ == "__main__":
    main()