# ♻️ Challenge #13 – Remove Duplicate Elements from a Sorted Linked List

## 📌 Problem Statement
Given a **sorted singly linked list**, remove all duplicate nodes so that each element appears **only once**.  
The operation should be performed **in-place** without using extra space.  

---

## 🚀 Solution
Since the list is sorted, any duplicates will be **next to each other**.  
We can simply traverse the list and check:
- If `current.data == current.next.data`, skip the `current.next` node.  
- Otherwise, move `current` forward.  

This ensures that only unique elements remain.

---

## 🧩 Example Walkthrough

Suppose the linked list is:  
`3 -> 5 -> 5 -> 7 -> 8 -> 10 -> 10 -> 10 -> 20 -> null`

Steps:
1. Start at `3`. Next is `5` → no duplicate → move ahead.  
2. At `5`. Next is `5` → duplicate found → remove the second `5`.  
   List becomes: `3 -> 5 -> 7 -> 8 -> 10 -> 10 -> 10 -> 20`.  
3. At `5`. Next is `7` → no duplicate → move ahead.  
4. At `10`. Next is `10` → remove duplicate.  
   List becomes: `3 -> 5 -> 7 -> 8 -> 10 -> 10 -> 20`.  
5. Still at `10`. Next is `10` → remove duplicate again.  
   List becomes: `3 -> 5 -> 7 -> 8 -> 10 -> 20`.  
6. At `20`. End of list → stop.  

✅ Final List: `3 -> 5 -> 7 -> 8 -> 10 -> 20 -> null`

---

## ⏱️ Complexity Analysis
- **Time Complexity**:  
  - O(n) → Each node is visited at most once.  
- **Space Complexity**:  
  - O(1) → No extra data structures used, only pointer manipulation.  

---

## 🎯 Key Takeaways
- The **sorted property** makes it easy to detect duplicates.  
- Only **one traversal** is needed.  
- This is the optimal solution.