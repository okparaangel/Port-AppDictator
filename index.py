# create a python file that can take any port number and 
# dictate the particular application name that is running on that port.

import socket

def get_application_name(port):
    try:
        return socket.getservbyport(port)
    except OSError as e:
        return f"Unknown ({e})"

if __name__ == "__main__":
    port = int(input("Enter port number: "))
    application_name = get_application_name(port)
    print(f"Application name for port {port}: {application_name}")
