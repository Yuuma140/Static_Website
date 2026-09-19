# Exponential Time & P vs NP

**Core Idea:** Some problems can be solved efficiently (P), others can only be verified efficiently (NP), and the relationship between them is unproven.

## How It Works

- **P** — solvable in polynomial time
- **NP** — verifiable in polynomial time
- **NP-complete** — hardest problems in NP, all NP problems reduce to it
- **NP-hard** — at least as hard as NP, doesn't need to be in NP

## Complexity

Naive recursive branching (e.g. fibonacci) = O(2^n). One recursive call per step = O(n).

## Code Pattern

**Exponential — two branches per call**

```
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

**Polynomial — one call per step, or memoized**

## When To Use

Recognize when a brute-force approach is exponential — signals you need memoization, a different algorithm, or acceptance that the problem is genuinely hard.

[Back to home](/)