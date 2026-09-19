# BFS and DFS

**Core Idea:** Two strategies for traversing a graph — breadth first (level by level) vs depth first (as deep as possible).

## How It Works

- **BFS** — uses a QUEUE, visits neighbors level by level
- **DFS** — uses a STACK (or recursion), goes deep before backtracking

## Complexity

Both O(V + E) — vertices plus edges.

## Code Pattern

**BFS and DFS**

```
queue = deque([start])
visited = set()
stack = [start]
```

**or recursive calls**

## When To Use

- BFS → shortest path in unweighted graph, level-order needs
- DFS → exploring all paths, cycle detection, backtracking problems

[Back to home](/)