import socket

target = input("Enter the IP address or hostname to scan: ")
min_port = int(input("Enter the minimum port number: "))
max_port = int(input("Enter the maximum port number: "))

# Loop over the range of ports to scan
for port in range(min_port, max_port + 1):
    # Create a new socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Set a timeout for the connection attempt
    
    # Try to connect to the target on the current port
    result = s.connect_ex((target, port))
    
    # Check if the connection was successful
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
    
    s.close()
