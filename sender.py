import socket
import struct 
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ttl = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,ttl)
sock.sendto("robot", (MCAST_GRP, MCAST_PORT))
