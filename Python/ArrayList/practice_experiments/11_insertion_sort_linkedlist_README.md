📘 README-Style Explanation (for Challenge #11)
🔢 Challenge #11 – Insertion Sort on a Linked List

📌 Problem Statement:
Implement Insertion Sort on a singly linked list. The linked list should be rearranged in ascending order.

🛠️ Approaches Implemented
1. Data Swap Version

Traverse the list with two pointers (unsorted and current).

Compare unsorted with all previous nodes.

Swap values whenever a smaller element is found.

✅ Simpler to implement but modifies node values instead of re-linking.

2. Node Re-link Version

Use a dummy node to simplify insertions at the head.

Remove nodes one by one from the unsorted portion and insert them into the correct position in the sorted portion.

✅ True linked list manipulation: no data swapping, only pointer re-linking.

⏱️ Complexity Analysis

| Approach          | Time Complexity | Space Complexity | Notes                                            |
| ----------------- | --------------- | ---------------- | ------------------------------------------------ |
| Data Swap Version | O(n²)           | O(1)             | Multiple data swaps, not pointer-friendly        |
| Re-link Version   | O(n²)           | O(1)             | Efficient pointer usage, preferred in interviews |