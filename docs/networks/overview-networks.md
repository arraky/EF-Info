## Switch

A switch facilitates the communication within a network. It combines the advantages of having a hub and a bridge: 

You connect every device within a network to the switch, the switch then accepts messages and repeats them to the intended location. It's thus possible to only communicate to one other device, instead of to the whole network. They enable the Hop to Hop of data and are thus, like Network Interface Card **NIC**, part of the second layer in the OSI model.

## MAC-Address
MAC-addresses are used to *address* communication between two devices. MAC-addresses are part of the 2nd level in the OSI model (used between NIC) There are 6 bytes, i.e. 48 bits, which are represented by 12 hex numbers:
```powershell
MAC Address:               #9465.9C3B.8AE5
Also written like this:   #94-65-9C-3B-8A-E5 / 94:65:9C:3B:8A:E5
```
**IMPORTANT**: Each MAC-address is unique

## IP Address

It's a device's address within a network. Part of the 3rd layer in the OSI model. 32 bits, 4 bytes, each 0-255.

**Network section**: Shows the network in which the device navigates. Edubern for instance: 10.166.2xx.xxx

**Host section**: This part is specific to the individual device. Every host section within a network is unique. For instance 10.166.227.92 is a possible host ip in the Edubern network.

**The net mask**: This 4 byte number shows how far the network section extends. To find that out, you have to write out the net mask in binary. 

```powershell
#Edubern's net mask:
255.255.240.0 
11111111.11111111.11110000.00000000 # (in binary) This means that the network can have 16*256=4096 different IPs
```
If you now write down a netmask in its binary form and directly below it any IP address, also in binary form, the 1's in the netmask mark those bits of the IP address which form the network part. The 0 in the netmask then mark the host part. You can also give information about the number of 1s in a netmask using a suffix. 


```powershell
Netmask:        255.255.240.0 
IP:             10.166.227.92

Binary:
Netmask:        11111111.11111111.11110000.00000000
IP:             00001010.10100110.11100011.10111000


Network section:00001010.10100110.1110
#               ^^^^^^^^^^^^^^^^^^^^^^
User section:                         0011.10111000
#                                     ^^^^^^^^^^^^^
IP with suffix: 10.166.227.92/20
```

### Number of special IPs
The broadcast-IP is used to send a message to everyone in your network, or even a foreign one. This IP is found by setting the whole user/host section to 1. No one device can have this IP
```powershell
Broadcast IP:   00001010.10100110.11101111.11111111 

Decimal: 10.166.239.255
#                                     ^^^^^^^^^^^^^
```
**127.0.0.1:** Loopback-d lets the device address itself

**0.0.0.0:** Placeholder, can stand for three things: No valid IP / any IP / your network

**IPs within range 224.0.0.0 to 239.255.255.255:** Multicast-addresses to send packets to many IPs (not all) at the same time

**Reserved for the creation of private networks:** This way, you can have two same IPs and that doesn't cause any issues as long as they are isolated from each other
```powershell
10.0.0.0 to 10.255.255.255

172.16.0.0 to 172.31.255.255

192.168.0.0 to 172.168.255.255
```
For the communication with the internet, IPs are translate into a new public IP address, this is called **NAT** (Network Address Translation)

## Router

Facilitates communication in between networks. The whole Internet is just a bunch of routers that link up different networks for worldwide communication.

Just like a switch, the router knows where a messages should be sent to, it thus only sends the message to the intended receiver.
Part of the 3rd layer in the OSI model.

## Gateway

## MAC-table

## Routing-table

## Ethernet-Frame
Similar to the way mRNA is sent within a cell, Data is sent in a structured way in between computers too.

## ARP 
Address Resolution Protocol. Links L2 and L3 of the OSI model (MAC and IP)