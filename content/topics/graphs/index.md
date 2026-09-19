# Graphs

**Core Idea:** Nodes (vertices) connected by edges — trees are a special case of graphs.

## How It Works

Can have cycles, multiple paths, or be disconnected. Max edges for n nodes = n(n-1)/2.

## Code Pattern

```
graph = {
    "A": ["B", "C"],
    "B": ["A"],
}
```

## When To Use

Networks, relationships, maps, dependencies — anything with many-to-many connections.

[Back to home](/)