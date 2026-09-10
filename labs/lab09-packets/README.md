# Lab 09 — Packet Analysis

## Objective
Learn to reason about network communication at the packet level.

## Concepts
- Ethernet frames
- IP packets
- TCP/UDP segments and datagrams
- ICMP
- DNS
- HTTP
- Packet fields
- Capture filters

## Exercises
1. Generate safe traffic such as ping, DNS, or HTTP requests in an authorized environment.
2. Capture traffic where the platform permits packet capture.
3. Identify protocols and source/destination information.
4. Follow one simple communication flow.
5. Explain each observed layer.

## Android Note
Unrooted Android may not permit traditional packet capture from Termux. If capture is unavailable, use another authorized lab environment or analyze provided captures.

## Questions
- What is the difference between a frame and an IP packet?
- Which information belongs to IP and which belongs to TCP?
- Why can encrypted HTTPS traffic still reveal some metadata?
