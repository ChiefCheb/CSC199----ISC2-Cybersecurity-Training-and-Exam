"""
This is the python script I used to try to automate the attack. 
I did get it to run after a bit of debugging but didn't get to implementing
the actual code to try and overload the buffer before the CTF ended.
"""

import socket, ssl

HOST = "hexv.challs.pwnoh.io"
PORT = 1337
CMD = "help\n"
RECV_BYTES = 4096
TIMEOUT = 3.0

ctx = ssl.create_default_context()

with socket.create_connection((HOST, PORT), timeout=5) as sock:
    with ctx.wrap_socket(sock, server_hostname=HOST) as ss:
        ss.settimeout(TIMEOUT)
        try:
            banner = ss.recv(RECV_BYTES)
        except Exception:
            banner = b''

        print("BANNER (raw):", banner)
        print("BANNER (text):", banner.decode('utf-8', errors='replace'))

        ss.sendall(CMD.encode())

        try:
            reply = ss.recv(RECV_BYTES)
        except socket.timeout:
            reply = b''

        print("REPLY (raw):", reply)
        print("REPLY (text):", reply.decode('utf-8', errors='replace'))
