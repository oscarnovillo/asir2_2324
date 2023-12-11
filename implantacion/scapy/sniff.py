from scapy.all import *
from scapy.layers import http  # import HTTP packet
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.tls.record import TLS


def process_packet(packet : Packet):
#  print(packet.summary()) 
#  print(packet.layers())
 if (packet.haslayer(TLS)):
#   print("HTTPs Request: ", packet.fields)
#   print("HTTPs Request: ", packet[TLS].msg[0].name)
  if ( "Client Hello" in packet[TLS].msg[0].name):
    print("Client Hello")
    for extension in packet[TLS].msg[0].ext:
        # print(extension.name)
        if ("Server Name" in extension.name):
            print("Server Name: ", extension.servernames[0].servername.decode())
            # extension.show()
    # print(packet[TLS].msg[0].fields)
  



load_layer("tls")
sniff(prn=process_packet)
