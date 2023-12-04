from scapy.all import *
from scapy.layers import http  # import HTTP packet
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.tls.record import TLS


def process_packet(packet : Packet):
#  print(packet.summary()) 
#  print(packet.layers())
 if (packet.haslayer(TLS)):
  print("HTTPs Request: ", packet.fields)
  print(packet[TLS])

load_layer("tls")
t = AsyncSniffer(prn=process_packet)
t.start()
t.join()
