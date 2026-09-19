# Big-O Notation

**Core Idea:** Describes how time/space requirements grow relative to input size.

## How It Works

Measures worst case by default. Drop constants and smaller terms — only the dominant growth term matters at scale.

## Growth Scale

- O(1) — constant
- O(log n) — logarithmic
- O(n) — linear
- O(n log n) — linearithmic
- O(n²) — quadratic
- O(2^n) — exponential
- O(n!) — factorial

## Code Pattern

```
for i in range(n):        # O(n)
for i in range(n):        # O(n²) when nested
    for j in range(n):
```

## When To Use

Analyze every loop or recursive function before considering a solution complete.

[Back to home](/)