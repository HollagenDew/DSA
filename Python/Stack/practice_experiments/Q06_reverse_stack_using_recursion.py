# 📁 File: Q06_reverse_stack_using_recursion.py
# 📌 Purpose: Reverse a stack using recursion (no extra stack allowed)
# 📚 Category: Stack – Recursion Based Problem
# 🧠 Description:
#   - Reverses a stack without using another stack
#   - Uses call stack + recursion to insert elements at bottom
#   - Demonstrates stack memory behavior (LIFO)
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-29

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, value) -> None:
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow — nothing to pop")
            return None
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def insert_at_bottom(self, value) -> None:
        """
        Insert element at bottom using recursion.
        Key step for stack reversal without extra DS.
        """
        if self.is_empty():
            self.push(value)
            return
        
        top = self.pop()
        self.insert_at_bottom(value)
        self.push(top)

    def reverse(self) -> None:
        """
        Recursively pop all items & push them at bottom.
        This reverses the original stack in-place.
        """
        if self.is_empty():
            return
        
        top = self.pop()
        self.reverse()
        self.insert_at_bottom(top)

    def __repr__(self) -> str:
        return f"Stack(bottom -> top): {self.items}"


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print(f"📦 Original Stack: {stack.items}")

    stack.reverse()

    print(f"🔁 Reversed Stack: {stack.items}")
