# Binary Trees (BST)

**Core Idea:** Hierarchical structure — left child smaller, right child larger than parent.

## How It Works

Each node has at most two children. Search/insert by comparing and moving left or right.

## Complexity

Balanced — O(log n) search/insert/delete. Unbalanced — degrades to O(n).

## Code Pattern

```
class BSTNode:
    def insert(self, val):
        if val < self.val:
            go left
        else:
            go right
```

## When To Use

Ordered data requiring fast search, insert, delete, and range queries.

[Back to home](/)