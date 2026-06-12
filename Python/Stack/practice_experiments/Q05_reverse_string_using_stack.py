# 📁 File: 05_reverse_string_using_stack.py
# 📌 Purpose: Reverse a given string using Stack (no slicing or built-ins)
# 📚 Category: Stack – Practical Application
# 🧠 Description:
#   - Uses stack operations (push & pop) to reverse a string
#   - Demonstrates real-world use of LIFO behavior
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-28

class Stack:
    def __init__(self, capacity: int = 100) -> None:
        self.items = []
        self.capacity = capacity

    def push(self, element) -> None:
        if self.is_full():
            print("⚠️ Stack Overflow! Cannot push — stack is full.")
        else:
            self.items.append(element)

    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow! Cannot pop — stack is empty.")
            return None
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.capacity

    def reverse_string(self, text: str) -> str:
        for char in text:
            self.push(char)

        reversed_chars = []
        while not self.is_empty():
            reversed_chars.append(self.pop())

        reversed_string = ''.join(reversed_chars)
        print(f"🧱 Original String: {text}")
        print(f"🔁 Reversed String: {reversed_string}")
        return reversed_string


if __name__ == "__main__":
    stack = Stack()
    stack.reverse_string("Prateek")
