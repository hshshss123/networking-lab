# Lab 10 — Network Troubleshooting

## Objective
Combine the previous labs into a structured troubleshooting method.

## Troubleshooting sequence

```text
1. Is the local network stack working?
        ↓
2. Can I reach the local network?
        ↓
3. Can I reach an Internet IP?
        ↓
4. Does DNS resolution work?
        ↓
5. Does the application protocol work?
```

## Exercises
1. Start with the simplest test.
2. Change only one variable at a time.
3. Record the command and exact output.
4. Identify the failing layer or component.
5. State what evidence supports the conclusion.
6. State what remains unknown.

## Example

If an Internet IP responds to ping but a domain lookup times out:

- IP connectivity has evidence of working.
- DNS resolution has a problem or restriction.
- It would be incorrect to conclude that the entire Internet connection is down.

## Questions
- Why should troubleshooting move from simple tests to more complex tests?
- Why is changing many settings at once bad troubleshooting practice?
- What evidence would distinguish DNS failure from HTTP failure?
