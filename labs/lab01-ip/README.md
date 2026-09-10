# Lab 01 — IP & Network Identity

## Objective
Understand how a device identifies itself on a network.

## Concepts
- Network interfaces
- IPv4 addresses
- Netmasks
- CIDR
- Network address
- Broadcast address
- Loopback

## Android/Termux
Some interface information may be available through `ifconfig`, while commands that require privileged Android networking access may fail.

## Exercises
1. List the interfaces available to Termux.
2. Identify the Wi-Fi interface.
3. Record its IPv4 address and netmask.
4. Convert the netmask to CIDR notation.
5. Calculate the network and broadcast addresses.
6. Explain what each result proves and what it does not prove.

## Questions
- What is your device's local IP?
- What network does that IP belong to?
- Why is `127.0.0.1` different from a Wi-Fi address?
- Why can two devices have different IP addresses but belong to the same network?
