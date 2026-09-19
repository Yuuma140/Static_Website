# Queues

**Core Idea:** FIFO — First In, First Out — like a line at a shop.

## How It Works

Add to back, remove from front.

## Complexity

enqueue, dequeue — O(1) using deque (O(n) with plain list)

## Code Pattern

```
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
```

## When To Use

Task scheduling, print queues, BFS implementation.

[Back to home](/)