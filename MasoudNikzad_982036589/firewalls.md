# firewalls
A firewall is a security device that monitors network traffic. It protects the internal network by filtering incoming and outgoing traffic based on a set of established rules. Setting up a firewall is the simplest way of adding a security layer between a system and malicious attacks


# How Does a Firewall Work?
Each data packet consists of a header (control information) and payload (the actual data). The header provides information about the sender and the receiver. Before the packet can enter the internal network through the defined port, it must pass through the firewall. This transfer depends on the information it carries and how it corresponds to the predefined rules.

# types of firewalls

### 1. software firewalls
it's a software that we install it in our machine.(many of os has installed a firewall by default)
It's easy to configure 
the big disadvantage of this firewall is if you have multiple computer in your organization you need to install and configure and maintain it on each machine

### 2. hardware firewalls
hardware firewalls are security devices that represent a separate piece of hardware placed between an internal and external network (the Internet)
hard to configure 
since the hardware firewall has its own cpu and ram it uses own resources

## types of firewalls bases on method operation
### 1. Packet-Filtering Firewalls
As explained above, each data packet consists of a header and the data it transmits. This type of firewall decides whether a packet is allowed or denied access based on the header information. To do so, it inspects the protocol, source IP address, destination IP, source port, and destination port. Depending on how the numbers match the access control list (rules defining wanted/unwanted traffic), the packets are passed on or dropped
### 2. Circuit-Level Gateways
it protects a network by forwarding requests from the original client and masking it as its own. Proxy means to serve as a substitute and, accordingly, that is the role it plays. It substitutes for the client that is sending the request
#### 3. Next-Generation Firewalls
NGFW checks the actual payload of the packet instead of focusing solely on header information


