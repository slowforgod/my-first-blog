import socket

def start_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '0.0.0.0'
    port = 8000
    
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Socket Server 실행 중: {host}:{port}")
    print("클라이언트 연결 대기...\n")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"연결됨: {addr}\n")
        
        request_data = client_socket.recv(4096).decode('utf-8')
        
        # 파일로 저장
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        # request 폴더 생성
        import os
        os.makedirs('request', exist_ok=True)
        
        filename = f"request/{timestamp}.bin"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(request_data)
        
        print("="*70)
        print(f"파일 저장: {filename}")
        print("="*70)
        print(request_data)
        print("="*70)
        
        response = "HTTP/1.1 200 OK\r\n\r\nReceived"
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    try:
        start_socket_server()
    except KeyboardInterrupt:
        print("\n서버 종료")