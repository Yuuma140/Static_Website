# Tries

**Core Idea:** Tree structure where each path from root represents a string, built from nested character mappings.

## How It Works

Each node holds children mapped by character. Following a path spells out a word.

## Complexity

Insert/search O(m) where m = word length, not dependent on number of words stored.

## Code Pattern

```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

## When To Use

Autocomplete, prefix search, spell check, dictionary lookups.

[Back to home](/)