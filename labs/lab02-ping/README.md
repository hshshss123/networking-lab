# Lab 02 — Ping & ICMP

## Objective
Understand how `ping` tests IP-layer reachability and measures round-trip time.

## Concepts
- ICMP Echo Request
- ICMP Echo Reply
- Packet loss
- Latency
- RTT
- Jitter/latency variation

## Exercises
1. Ping your own loopback address.
2. Ping a known device on your authorized local network.
3. Ping a public IP such as `8.8.8.8`.
4. Record transmitted packets, received packets, loss, and RTT.
5. Compare local and Internet latency.

## Important
A successful ping proves that ICMP traffic received replies. It does **not** prove that DNS, HTTP, SSH, or every other service is working.

## Questions
- What does 0% packet loss mean?
- Why can RTT vary between packets?
- Why might a host be reachable but a website on that host unavailable?
