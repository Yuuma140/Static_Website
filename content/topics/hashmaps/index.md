# Hashmaps

**Core Idea:** Key-value storage using a hash function to compute array index directly.

## How It Works

Hash function converts key into an array index. Collisions handled via chaining or open addressing.

## Complexity

O(1) average for insert/search/delete. O(n) worst case with heavy collisions.

## Code Pattern

```
my_dict = {}
my_dict["key"] = "value"
```

## When To Use

Fast lookups by key, counting frequencies, caching/memoization.

[Back to home](/)