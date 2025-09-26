# 🔢 Challenge #12 – Find the Nth Node from the End of a Singly Linked List in One Pass

## 📌 Problem Statement

Given a singly linked list, return the **Nth node from the end** in **one traversal**.

* The last node = 1st from end
* The second last node = 2nd from end, and so on.

If `n` is larger than the list length, raise an exception.

---

## 🚀 Solution – One-Pass Approach (Two-Pointer Technique)

1. Initialize two pointers: `slow` and `fast` at the head.
2. Move the `fast` pointer **n steps ahead**.

   * If `fast` becomes `null` before completing `n` steps, `n` exceeds list length.
3. Move both `slow` and `fast` one step at a time until `fast` reaches the end.
4. At this point, `slow` points at the **Nth node from the end**.

* **Time Complexity**: O(n) → only one traversal
* **Space Complexity**: O(1)

---

## 🧩 Example Walkthrough

Suppose the linked list is:

```
46 -> 12 -> 32 -> 87 -> 19 -> null
```

We want the **2nd node from the end**.

1. Start with both `slow` and `fast` at `46`.

```
slow = 46, fast = 46
```

2. Move `fast` ahead by 2 steps:

```
Step 1: fast = 12
Step 2: fast = 32
```

3. Now move both one step at a time:

```
slow = 46, fast = 32
→ move → slow = 12, fast = 87
→ move → slow = 32, fast = 19
→ move → slow = 87, fast = null
```

4. When `fast` reaches `null`, `slow` is at **87**.

✅ **Output:** `87` is the 2nd node from the end.