import socket,sys
import impacket.ImpactPacket as packet
import time

src = sys.argv[1]
dst = sys.argv[2]
ip = packet.IP()
ip.set_ip_src(src)
ip.set_ip_dst(dst)

icmp = packet.ICMP()
icmp.set_icmp_type(icmp.ICMP_ECHO)
#icmp.contains(packet.Data("a"*100))
ip.contains(icmp)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
icmp.set_icmp_id(1)
icmp.set_icmp_cksum(0)
icmp.auto_checksum = 0
while True: 
     s.sendto(ip.get_packet(), (dst, 0))
     time.sleep(1)
