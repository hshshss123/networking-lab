# Networking Lab

A hands-on, terminal-based networking tutor for beginners.

The project is designed primarily for **Android + Termux**, but the Python tutor also works on normal Linux environments.

## What makes this different?

This is not intended to be a static list of networking commands.

Run the tutor in your terminal and learn interactively:

```text
NETWORKING LAB — INTERACTIVE TUTOR

Choose a lab:

  01. IP & Network Identity
  02. Ping & ICMP
  03. Gateway & Routing
  04. DNS
  05. TCP/UDP & Ports
  06. HTTP/HTTPS
  07. Traceroute
  08. ARP & MAC
  09. Packet Analysis
  10. Network Troubleshooting
```

The tutor explains **why** a command is being used, runs safe diagnostics, shows the result, and asks questions so you have to reason about what you observed.

## Learning method

Every lab follows this cycle:

1. Learn the concept.
2. Understand why a test is useful.
3. Run the test.
4. Observe the actual output.
5. Interpret the result.
6. Answer a question or challenge.
7. Learn what the test **cannot** prove.

This is intended to build troubleshooting and security-analysis habits rather than command memorization.

## Termux Setup

### 1. Install Termux

Install Termux from a trusted source such as the official Termux project distribution. Avoid downloading random APK copies.

### 2. Update Termux

Open Termux and run:

```bash
pkg update -y && pkg upgrade -y
```

This updates the package lists and installed packages.

### 3. Install the tools used by the labs

```bash
pkg install -y python git iproute2 dnsutils curl openssh nano
```

These provide Python, Git, common networking utilities, and a text editor.

> `tcpdump` is intentionally not required by the core tutor. Availability of low-level packet-capture tools can vary by Android/Termux environment and permissions.

### 4. Clone this repository

```bash
git clone https://github.com/hshshss123/networking-lab.git
```

This downloads the project to your Termux home directory.

### 5. Enter the project

```bash
cd networking-lab
```

### 6. Check Python

```bash
python --version
```

The tutor uses the Python standard library, so no third-party Python packages are required.

### 7. Start the tutor

```bash
python networking_lab.py
```

You should see the interactive menu.

## Quick Setup

Once you understand the individual steps above, the setup can be done with:

```bash
pkg update -y && pkg upgrade -y
pkg install -y python git iproute2 dnsutils curl openssh nano
git clone https://github.com/hshshss123/networking-lab.git
cd networking-lab
python networking_lab.py
```

## Labs

| Lab | Topic | What you learn |
|---|---|---|
| 01 | IP & Network Identity | Interfaces, IPv4, netmasks, subnets |
| 02 | Ping & ICMP | Reachability, latency, packet loss |
| 03 | Gateway & Routing | Routes, gateways, next hops |
| 04 | DNS | Name resolution and DNS failures |
| 05 | TCP/UDP & Ports | Transport protocols and ports |
| 06 | HTTP/HTTPS | Requests, responses, TLS concepts |
| 07 | Traceroute | Hops, TTL, routing paths |
| 08 | ARP & MAC | Local IP-to-MAC resolution |
| 09 | Packet Analysis | Protocol and packet concepts |
| 10 | Troubleshooting | Structured network diagnosis |

## Android / Termux Limitations

Android applies security restrictions that differ from a conventional Linux installation.

You may encounter:

- Permission errors when accessing kernel networking information.
- Incomplete interface information.
- Restricted routing-table access.
- Limited access to ARP/neighbor information.
- Packet-capture limitations on unrooted devices.

These failures are themselves useful lessons. **Do not assume that a command failing means the network is broken.**

## Safety

The labs are designed for your own device, your own network, or systems for which you have explicit authorization.

Do not use the project to scan, intercept, disrupt, or attack systems without permission.

## Project Structure

```text
networking-lab/
├── labs/
├── scripts/
├── docs/
├── networking_lab.py
├── requirements.txt
└── README.md
```

## Long-Term Roadmap

After the first 10 labs, the project can grow into:

- Subnetting challenges
- Python socket programming
- Network monitoring
- Service discovery in an authorized lab
- Controlled port-scanning exercises
- Packet-capture analysis
- Network security fundamentals
- Cybersecurity troubleshooting scenarios

The goal is to progress from **"What command do I run?"** to **"What evidence do I need to determine what is happening?"**
