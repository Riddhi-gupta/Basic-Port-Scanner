import socket
from threading import Thread, Lock

class PortScanner:
    def __init__(self, host, start_port, end_port):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
        self.lock = Lock()

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.host, port))
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def scan(self):
        threads = []
        for port in range(self.start_port, self.end_port + 1):
            thread = Thread(target=self.scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.display_results()

    def display_results(self):
        if self.open_ports:
            print(f"Open ports on {self.host}:")
            for port in self.open_ports:
                print(f"Port {port} is open.")
        else:
            print(f"No open ports found on {self.host}.")

if __name__ == "__main__":
    host = input("Enter the host IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scanner = PortScanner(host, start_port, end_port)
    scanner.scan()
