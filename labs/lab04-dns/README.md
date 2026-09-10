# Lab 04 — DNS

## Objective
Understand how domain names are resolved into IP addresses and how DNS failures differ from general connectivity failures.

## Concepts
- DNS query
- Resolver
- A and AAAA records
- DNS server
- Timeout
- Name resolution
- Private DNS

## Exercises
1. Resolve a domain using the normal system resolver.
2. Test an explicitly selected DNS resolver where the network permits it.
3. Compare DNS resolution with direct IP connectivity.
4. Record successful responses and timeouts.
5. Explain exactly what each test proves.

## Troubleshooting Question
If `ping 8.8.8.8` works but a DNS query times out, Internet connectivity and DNS resolution should be treated as separate questions.

## Questions
- What does DNS translate?
- What is the difference between a DNS server and the website server?
- Why can DNS fail while IP connectivity still works?
- Why might direct queries to a public DNS server be blocked?
