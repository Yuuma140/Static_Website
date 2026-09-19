# Sorting Algorithms

**Core Idea:** Different tradeoffs between time, space, and stability for ordering data.

## How It Works

- **Bubble** — compares adjacent pairs, bubbles largest to end
- **Insertion** — builds sorted portion, walks new elements left
- **Selection** — finds minimum, one swap per pass
- **Merge** — splits in half recursively, merges back sorted
- **Quick** — picks pivot, partitions smaller/larger, recurses

## Complexity

- **Bubble** — Best: O(n), Avg: O(n²), Worst: O(n²), Space: O(1), Stable: Yes
- **Insertion** — Best: O(n), Avg: O(n²), Worst: O(n²), Space: O(1), Stable: Yes
- **Selection** — Best: O(n²), Avg: O(n²), Worst: O(n²), Space: O(1), Stable: No
- **Merge** — Best: O(n log n), Avg: O(n log n), Worst: O(n log n), Space: O(n), Stable: Yes
- **Quick** — Best: O(n log n), Avg: O(n log n), Worst: O(n²), Space: O(log n), Stable: No

## When To Use

- Small/nearly sorted → Insertion
- Guaranteed performance → Merge
- General purpose → Quick

[Back to home](/)