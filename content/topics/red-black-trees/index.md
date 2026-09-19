# Red Black Trees

**Core Idea:** Self-balancing binary tree using color rules to guarantee O(log n).

## How It Works

Every node red or black, root always black, no two adjacent red nodes, equal black-height on every path. Rotations restore these rules after insert/delete.

## Complexity

Guaranteed O(log n) for search/insert/delete, even worst case.

## Code Pattern

```
def rotate_left(self, pivot_parent):
    pivot = pivot_parent.right
    pivot_parent.right = pivot.left
    # reassign parent pointers
```

## When To Use

When guaranteed balanced performance matters more than simplicity — used internally in many language libraries.

[Back to home](/)