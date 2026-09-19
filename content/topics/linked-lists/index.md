# Linked Lists

**Core Idea:** Elements connected via pointers rather than index-based contiguous memory.

## How It Works

Each node holds a value and a pointer to the next node. No direct index access — must traverse from the head.

## Complexity

Insert/delete at known node — O(1). Search/access by position — O(n).

## Code Pattern

```
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

## When To Use

Frequent insertions/deletions where order matters more than random access.

[Back to home](/)