# Repository for project 0x08. Networking basics #1

## Terminology:
* Localhost:
Is a way "to call" this computer in the context of networking.
127.0.0.1 is the localhost. The address is used to establish an IP connection to the same machine or computer that the end user uses. Also, when a service is listening on 127.0.0.1 the service is only bound to the loopback interface (only available on the local machine)

* 0.0.0.0:
All IPv4 addresses on the local machine. When a service is listening on 0.0.0.0 this means the service is listening on all the configured network interfaces.

* Hosts file:
The hosts file is used to map hostnames (in other words domains) to IP addresses. With the hosts file the user can change the IP address that resolve a given domain name to. This change only affects the own computer without affecting how the domain is resolved worldwide. It is found in /etc/hosts

* ifconfig:
Is refers to interface configuration. It is used to view and change the configuration of the network interfaces on the system. When I running the command ifconfig on Ubuntu, the output shows information about all network interfaces currently in operation. **The output includes: eth0, lo and wlan. These are the names of the active network interfaces on the system.** **eth0 is the first Ethernet interface (There are eth1, eth2, etc). **lo is the loopback interface. This is a special network interface that the system uses to communicate with itself. **wlan is the name of the first wireless network interface on the system, (There are wlan1, wlan2n etc)
