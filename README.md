# Networking Lab

A hands-on networking learning project for beginners, built around real observations from a device and network.

The initial environment is **Android + Termux**, so the project also documents what Android allows, what it restricts, and how to reason from incomplete network information.

## Goal

Learn networking by doing experiments instead of memorizing definitions.

Each lab follows the same method:

1. Run a command or script.
2. Understand **why** it was used.
3. Record the output.
4. Explain what the result means.
5. Separate what was **observed** from what is only an **assumption**.
6. Identify what the test cannot prove.

That last step is important for real troubleshooting and cybersecurity work.

## Labs

| Lab | Topic | Main concepts |
|---|---|---|
| 01 | IP & Network Identity | Interfaces, IPv4, netmask, subnet, broadcast |
| 02 | Ping & ICMP | Reachability, latency, packet loss |
| 03 | Gateway & Routing | Default gateway, routes, next hop |
| 04 | DNS | Names, IP resolution, DNS servers, failure analysis |
| 05 | TCP/UDP & Ports | Transport layer, ports, connections |
| 06 | HTTP/HTTPS | Requests, responses, headers, TLS basics |
| 07 | Traceroute | Hops, TTL, routing path |
| 08 | ARP & MAC | Local network discovery, MAC addresses |
| 09 | Packet Analysis | Packets, protocols, fields, captures |
| 10 | Network Troubleshooting | A structured troubleshooting workflow |

## Lab 01 — IP & Network Identity

Learn how a device identifies itself on a network.

Topics:

- Network interfaces
- Wi-Fi vs mobile-data interfaces
- IPv4 addresses
- Loopback (`127.0.0.1`)
- Netmasks
- CIDR notation
- Network address
- Broadcast address

Example observation from the Android/Termux environment:

```text
wlan0
IP:      10.10.50.156
Netmask: 255.255.252.0
```

The lab should teach how to calculate the corresponding network and broadcast addresses rather than simply displaying them.

## Lab 02 — Ping & ICMP

Learn how `ping` tests IP-layer reachability using ICMP Echo messages.

Topics:

- ICMP Echo Request
- ICMP Echo Reply
- Packet loss
- Round-trip time (RTT)
- Latency variation
- Why successful ping does not prove that every service is working

## Lab 03 — Gateway & Routing

Learn how a device decides where to send traffic.

Topics:

- Default gateway
- Routing table
- Destination networks
- Next hop
- Local vs remote traffic
- Android restrictions on low-level network information

Some Android devices restrict access to routing information from ordinary applications such as Termux. A failed command is therefore treated as a useful observation, not automatically as a broken network.

## Lab 04 — DNS

Learn how domain names are translated into IP addresses.

Topics:

- DNS queries
- Recursive resolvers
- A/AAAA records
- DNS server addresses
- DNS timeouts
- Difference between DNS failure and general Internet failure
- Android Private DNS and resolver behavior

A key exercise is comparing domain-based access with direct IP connectivity and explaining what each test actually proves.

## Lab 05 — TCP/UDP & Ports

Learn how applications communicate through transport-layer protocols.

Topics:

- TCP
- UDP
- Source and destination ports
- Listening services
- TCP connection establishment
- Why a port being reachable does not automatically mean a vulnerability exists

All testing must be performed only against systems the user owns or is explicitly authorized to test.

## Lab 06 — HTTP/HTTPS

Learn what happens when a browser or command-line client accesses a website.

Topics:

- HTTP requests
- HTTP responses
- Methods
- Status codes
- Headers
- HTTPS
- TLS at a conceptual level
- Hostnames and virtual hosting

The lab uses safe public websites for basic protocol observation and focuses on understanding normal traffic.

## Lab 07 — Traceroute

Learn how packets can reveal intermediate routing hops.

Topics:

- TTL / Hop Limit
- ICMP responses
- UDP-based traceroute
- Timeouts
- Private network hops
- Why traceroute results can be incomplete or misleading

## Lab 08 — ARP & MAC

Learn how IPv4 devices communicate with other devices on the same local network.

Topics:

- MAC addresses
- ARP requests
- ARP replies
- IP-to-MAC mapping
- Local broadcast
- Neighbor discovery concepts

Android permissions may restrict direct access to ARP/neighbor information. The lab documents those limitations instead of assuming the information is available.

## Lab 09 — Packet Analysis

Learn to think at the packet level.

Topics:

- Ethernet concepts
- IP headers
- TCP/UDP headers
- ICMP
- DNS
- HTTP
- Packet captures
- Filtering and protocol identification

Where packet capture is unavailable on Android, the lab can use a controlled capture from another authorized environment or inspect available command output instead.

## Lab 10 — Network Troubleshooting

Combine the previous labs into a repeatable troubleshooting process.

Example decision path:

```text
Can I reach localhost?
        |
        v
Can I reach the local network?
        |
        v
Can I reach an Internet IP?
        |
        v
Does DNS resolve names?
        |
        v
Does the application protocol work?
```

The objective is to identify **which layer or component is failing**, rather than randomly changing settings.

## Android + Termux Notes

Android is not a normal Linux distribution. Applications run under Android's security model and may not have access to kernel networking interfaces or privileged operations.

Therefore:

- Some Linux networking commands may fail with permission errors.
- Some interface information may be incomplete.
- Routing-table access may be restricted.
- Packet capture may require capabilities unavailable to an unrooted device.
- A command failure does not necessarily mean the network itself is broken.

These limitations are part of the learning material.

## Project Structure

```text
networking-lab/
├── labs/
│   ├── lab01-ip/
│   ├── lab02-ping/
│   ├── lab03-routing/
│   ├── lab04-dns/
│   ├── lab05-tcp-udp/
│   ├── lab06-http-https/
│   ├── lab07-traceroute/
│   ├── lab08-arp-mac/
│   ├── lab09-packets/
│   └── lab10-troubleshooting/
├── scripts/
├── docs/
└── README.md
```

## Safety

This project is for learning and authorized testing.

Only test:

- Your own device
- Your own home/lab network
- Systems where you have explicit permission to test

Do not scan, intercept, disrupt, or attack networks or systems without authorization.

## Progress

- [x] Project created
- [x] Learning roadmap created
- [ ] Lab 01 — IP & Network Identity
- [ ] Lab 02 — Ping & ICMP
- [ ] Lab 03 — Gateway & Routing
- [ ] Lab 04 — DNS
- [ ] Lab 05 — TCP/UDP & Ports
- [ ] Lab 06 — HTTP/HTTPS
- [ ] Lab 07 — Traceroute
- [ ] Lab 08 — ARP & MAC
- [ ] Lab 09 — Packet Analysis
- [ ] Lab 10 — Network Troubleshooting

## Long-Term Direction

After the core labs, the project can expand into:

- Subnetting exercises
- Python networking scripts
- Socket programming
- Local service discovery
- Controlled port scanning
- Network monitoring
- Log analysis
- Packet filtering
- Cybersecurity-focused network labs

The long-term goal is practical networking knowledge that can support **cybersecurity, system administration, troubleshooting, and programming**.