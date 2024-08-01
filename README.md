# Basic-Port-Scanner
# Objective
The objective of this project is to develop a basic port scanner that scans for open ports on a specified host. This tool can be used to identify open ports and services running on a networked device, which is an essential part of network security assessments.

# Scope
1.) Scan a range of ports on a given host.
2.) Identify open ports.
3.) Display the results in a user-friendly format.

# Architecture
The project consists of the following components:

1.) Scanner Module: Scans the specified host for open ports.
2.) Result Display Module: Displays the scan results in a readable format.

# Tools and Technologies
1.) Programming Language: Python
2.) Libraries: 
Socket (for network connections)
Threading (for concurrent scanning)

# Working
Initialization: The PortScanner class is initialized with the host IP address and the range of ports to scan.
Scanning Ports: For each port in the range, a separate thread is started to scan the port. The scan_port method attempts to connect to the specified port. If the connection is successful (i.e., the port is open), the port number is added to the open_ports list.
Displaying Results: After all threads have completed, the display_results method prints the open ports.

# Running the Project
To run the project, Save the code to a file named port_scanner.py and run it using the command:
{ python port_scanner.py}
You will be prompted to enter the host IP address and the range of ports to scan. The tool will then display the open ports on the specified host.

# Security and Ethical Considerations
Permission: Ensure you have explicit permission to scan the target host. Unauthorized scanning can be considered illegal and unethical. 
I made this project for my internship project submission
Scope: Keep the scope of your scans limited to prevent unintentional disruptions to services.
Responsible Use: Use this tool responsibly and only for educational or authorized security assessments.

