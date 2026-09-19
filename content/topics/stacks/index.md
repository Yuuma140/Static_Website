# Stacks

**Core Idea:** LIFO — Last In, First Out — like a stack of plates.

## How It Works

Add and remove only from the top.

## Complexity

push, pop, peek, isEmpty — all O(1)

## Code Pattern

```
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
```

## When To Use

Function call tracking, undo functionality, browser history, balanced bracket checking, DFS implementation.

[Back to home](/)