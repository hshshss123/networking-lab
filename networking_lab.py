#!/usr/bin/env python3
"""Interactive, beginner-friendly networking tutor for Termux/Linux.

The program teaches concepts while safely running read-only/local diagnostics.
It intentionally avoids intrusive scanning or attack functionality.
"""

import ipaddress
import platform
import re
import shutil
import socket
import subprocess
import sys
import urllib.request


def run(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:
        return 1, f"{type(e).__name__}: {e}"


def pause():
    input("\nPress ENTER to continue...")


def header(title):
    print("\n" + "=" * 58)
    print(title)
    print("=" * 58)


def explain(text):
    print("\nWHY:")
    print(text)


def ip_lab():
    header("LAB 01 — IP & NETWORK IDENTITY")
    print("An IP address identifies an interface on an IP network.")
    explain("We start here because every later networking test depends on knowing which interface and IP address are involved.")
    pause()

    print("\nRunning: ifconfig")
    code, out = run(["ifconfig"])
    print("\n--- OUTPUT ---")
    print(out or "No output")

    print("\nLook for:")
    print("  wlan0  = commonly the Wi-Fi interface on Android")
    print("  lo     = loopback; your device talking to itself")
    print("  ccmni* = commonly a mobile-data interface on Android")
    print("\nImportant: interface names can vary. Treat the output, not the expectation, as the evidence.")

    ips = re.findall(r"inet (\d+\.\d+\.\d+\.\d+).*?netmask (\d+\.\d+\.\d+\.\d+)", out, re.S)
    if ips:
        print("\nDetected IPv4 addresses:")
        for addr, mask in ips:
            try:
                iface = ipaddress.IPv4Interface(f"{addr}/{mask}")
                print(f"  {addr} / {mask}  -> network {iface.network.network_address}/{iface.network.prefixlen}, broadcast {iface.network.broadcast_address}")
            except ValueError:
                print(f"  {addr} / {mask}")

    print("\nCHECK YOUR UNDERSTANDING")
    print("If your IP is 192.168.1.20/24, which network is it on?")
    print("A) 192.168.0.0/24")
    print("B) 192.168.1.0/24")
    print("C) 192.168.1.20/32")
    ans = input("Answer: ").strip().lower()
    print("✓ Correct." if ans in ("b", "2") else "Not quite. The answer is B: 192.168.1.0/24.")
    pause()


def ping_lab():
    header("LAB 02 — PING & ICMP")
    print("Ping tests whether an IP endpoint responds to ICMP Echo messages and measures round-trip time.")
    explain("We use ping to separate basic IP reachability from higher-level problems such as DNS or HTTP failures.")
    target = input("\nEnter an IP or hostname to test [8.8.8.8]: ").strip() or "8.8.8.8"
    print(f"\nRunning: ping -c 4 {target}")
    code, out = run(["ping", "-c", "4", target])
    print("\n--- OUTPUT ---")
    print(out or "No output")
    if code == 0:
        print("\nOBSERVED: the target responded to this ICMP test.")
    else:
        print("\nOBSERVED: the ICMP test did not complete successfully.")
    print("CAUTION: ping success does NOT prove that DNS, TCP, HTTPS, or every application service works.")
    pause()


def routing_lab():
    header("LAB 03 — GATEWAY & ROUTING")
    print("A routing table tells the operating system where to send packets.")
    explain("We want to discover the path decision for local and remote destinations. Android may restrict routing-table access to unprivileged Termux processes.")
    if shutil.which("ip"):
        print("\nRunning: ip route")
        code, out = run(["ip", "route"])
        print("\n--- OUTPUT ---")
        print(out or "No output")
        if "Permission denied" in out:
            print("\nAndroid restricted this information. That is an important observation, not proof that routing is broken.")
    else:
        print("The 'ip' command is not installed.")
    pause()


def dns_lab():
    header("LAB 04 — DNS")
    print("DNS translates names such as example.com into IP addresses.")
    explain("We compare name resolution with direct IP connectivity so we can tell whether a failure is DNS-specific or more general.")
    host = input("\nHostname [example.com]: ").strip() or "example.com"
    print(f"\nRunning: nslookup {host}")
    if shutil.which("nslookup"):
        code, out = run(["nslookup", host])
        print("\n--- OUTPUT ---")
        print(out or "No output")
    else:
        print("nslookup is not installed.")
    try:
        print("\nPython resolver test:")
        print(socket.gethostbyname_ex(host))
    except Exception as e:
        print(f"Python resolver failed: {e}")
    print("\nKEY IDEA: successful IP ping and failed DNS resolution can happen at the same time.")
    pause()


def tcp_udp_lab():
    header("LAB 05 — TCP / UDP & PORTS")
    print("Ports identify application endpoints at the transport layer.")
    explain("Instead of scanning networks, this lab safely tests one explicitly chosen host and port with a short TCP connection attempt.")
    host = input("Host [example.com]: ").strip() or "example.com"
    port_text = input("TCP port [443]: ").strip() or "443"
    try:
        port = int(port_text)
        with socket.create_connection((host, port), timeout=5):
            print(f"\nOBSERVED: a TCP connection to {host}:{port} succeeded.")
    except Exception as e:
        print(f"\nOBSERVED: TCP connection failed or timed out: {e}")
    print("A successful connection only tells us that a TCP connection was possible at that moment; it does not prove the service is secure.")
    pause()


def http_lab():
    header("LAB 06 — HTTP / HTTPS")
    print("HTTP is an application protocol used to exchange requests and responses.")
    explain("We inspect a normal HTTPS response so you can connect DNS, TCP, TLS, HTTP headers, and status codes into one chain.")
    url = input("URL [https://example.com]: ").strip() or "https://example.com"
    if not re.match(r"^https?://", url):
        url = "https://" + url
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "networking-lab/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"\nStatus: {r.status}")
            print(f"Final URL: {r.geturl()}")
            print("\nHeaders:")
            for k, v in list(r.headers.items())[:12]:
                print(f"  {k}: {v}")
    except Exception as e:
        print(f"\nHTTPS request failed: {e}")
    pause()


def traceroute_lab():
    header("LAB 07 — TRACEROUTE")
    print("Traceroute attempts to reveal intermediate routing hops.")
    explain("It helps visualize that traffic normally crosses multiple routers between a device and a remote destination. Some hops may not reply.")
    target = input("Target [8.8.8.8]: ").strip() or "8.8.8.8"
    command = None
    if shutil.which("traceroute"):
        command = ["traceroute", "-m", "8", target]
    elif shutil.which("tracepath"):
        command = ["tracepath", "-m", "8", target]
    if command:
        print("\nRunning:", " ".join(command))
        code, out = run(command)
        print("\n--- OUTPUT ---")
        print(out or "No output")
    else:
        print("No traceroute/tracepath command is installed.")
        print("You can install an appropriate package later if your environment permits it.")
    print("\nDo not assume every timeout is a broken hop; routers may intentionally avoid responding to traceroute probes.")
    pause()


def arp_lab():
    header("LAB 08 — ARP & MAC")
    print("ARP helps IPv4 devices discover the MAC address associated with a local IP address.")
    explain("We inspect information already exposed by the operating system rather than performing active network discovery.")
    for command in (["ip", "neigh"], ["arp", "-a"]):
        if shutil.which(command[0]):
            print("\nRunning:", " ".join(command))
            code, out = run(command)
            print(out or "No output")
            if out:
                break
    else:
        print("No supported neighbor/ARP command is available.")
    print("\nAndroid may restrict neighbor-table access. Lack of output is not proof that ARP is not being used.")
    pause()


def packet_lab():
    header("LAB 09 — PACKET ANALYSIS")
    print("A packet is structured data moving through a network stack.")
    explain("This lab prepares you to read packet captures later. On unrooted Android, low-level packet capture may not be available, so we first inspect protocol-level evidence we can safely obtain.")
    print("\nConcept chain:")
    print("Application → TCP/UDP → IP → Link layer")
    print("\nExample: HTTPS")
    print("DNS name → IP → TCP connection → TLS → HTTP exchange")
    pause()


def troubleshooting_lab():
    header("LAB 10 — TROUBLESHOOTING CHALLENGE")
    print("You are given a common symptom: 'A website does not work.'")
    print("Your job is to test layers in a logical order.")
    print("\n1. Can the device reach a known IP?")
    print("2. Can DNS resolve a hostname?")
    print("3. Can TCP connect to HTTPS port 443?")
    print("4. Can an HTTPS request succeed?")
    print("\nThe lesson: do not jump directly to changing settings. Gather evidence first.")
    host = input("\nHostname to investigate [example.com]: ").strip() or "example.com"
    print("\n--- TEST 1: DNS ---")
    try:
        addresses = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
        ips = sorted({a[4][0] for a in addresses})
        print("Resolved:", ", ".join(ips))
    except Exception as e:
        print("DNS failed:", e)
        print("Likely area to investigate: name resolution.")
        pause()
        return
    print("\n--- TEST 2: TCP 443 ---")
    try:
        with socket.create_connection((host, 443), timeout=5):
            print("TCP 443: reachable")
    except Exception as e:
        print("TCP 443 failed:", e)
        print("Next area to investigate: routing, filtering, or service availability.")
        pause()
        return
    print("\n--- TEST 3: HTTPS ---")
    try:
        req = urllib.request.Request("https://" + host, method="HEAD", headers={"User-Agent": "networking-lab/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            print("HTTPS status:", r.status)
            print("Result: DNS, TCP, TLS/HTTPS all completed for this test.")
    except Exception as e:
        print("HTTPS failed:", e)
        print("DNS and TCP succeeded, so investigate above/beyond the HTTPS request layer.")
    pause()


def about():
    header("ABOUT THIS LAB")
    print("Networking Lab is an interactive terminal tutor for practical networking.")
    print("It is designed for Android + Termux and normal Linux environments.")
    print("\nPrinciples:")
    print("  • Understand every command before running it.")
    print("  • Record observations instead of guessing.")
    print("  • Learn what each test proves — and what it cannot prove.")
    print("  • Use only systems and networks you own or are authorized to test.")
    pause()


def main():
    labs = [
        ("01", "IP & Network Identity", ip_lab),
        ("02", "Ping & ICMP", ping_lab),
        ("03", "Gateway & Routing", routing_lab),
        ("04", "DNS", dns_lab),
        ("05", "TCP/UDP & Ports", tcp_udp_lab),
        ("06", "HTTP/HTTPS", http_lab),
        ("07", "Traceroute", traceroute_lab),
        ("08", "ARP & MAC", arp_lab),
        ("09", "Packet Analysis", packet_lab),
        ("10", "Network Troubleshooting", troubleshooting_lab),
    ]
    while True:
        header("NETWORKING LAB — INTERACTIVE TUTOR")
        print(f"Python: {platform.python_version()} | OS: {platform.system()} {platform.release()}")
        print("\nChoose a lab:")
        for n, title, _ in labs:
            print(f"  {n}. {title}")
        print("  A. About")
        print("  Q. Quit")
        choice = input("\nChoice: ").strip().lower()
        if choice == "q":
            print("\nKeep learning. Build the habit of testing before guessing.")
            return
        if choice == "a":
            about()
            continue
        selected = next((x for x in labs if x[0] == choice.zfill(2)), None)
        if selected:
            selected[2]()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting.")
        sys.exit(0)
