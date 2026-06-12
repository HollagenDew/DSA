# 📁 File: Q04_stack_count_elements.py
# 📌 Purpose: Add a method to count and return the number of elements in stack
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Tracks stack size manually using a counter
#   - Demonstrates stack growth and shrinkage with push/pop operations
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-28

class Stack:
    def __init__(self, capacity: int = 4) -> None:
        self.items = []
        self.capacity = capacity
        self.size = 0

    def push(self, element: int) -> None:
        if self.is_full():
            print("⚠️ Stack Overflow! Cannot push — stack is full.")
        else:
            self.items.append(element)
            self.size += 1
            print(f"✅ Pushed: {element}")

    def pop(self) -> None:
        if self.is_empty():
            print("⚠️ Stack Underflow! Cannot pop — stack is empty.")
        else:
            removed_element = self.items.pop()
            self.size -= 1
            print(f"🗑️ Popped: {removed_element}")

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def peek(self) -> None:
        if self.is_empty():
            print("⚠️ Stack is empty — nothing to peek.")
        else:
            print(f"👁️ Top element is: {self.items[-1]}")

    def count(self) -> int:
        print(f"📏 Size of the Stack is: {self.size}")
        return self.size


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.count()
    stack.pop()
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()  # ✅ fixed parentheses
    stack.peek()
    stack.count()
