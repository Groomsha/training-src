import socket


class SockBase:
    def __init__(self) -> None:
        self.server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(('127.0.0.1', 8585))
        self.server.listen()

        while True:
            self.client, addr = self.server.accept()
            print(f'Connection from: {addr}')

            while True:
                request = self.client.recv(4096)

                if not request:
                    break
                else:
                    response = "Hello world\n".encode()
                    self.client.send(response)

            self.client.close()


if __name__ == '__main__':
    socket = SockBase()