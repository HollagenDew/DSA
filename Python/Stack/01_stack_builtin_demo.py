# 📁 File: 01_stack_builtin_demo.py
# 📌 Purpose: Demonstrate basic stack operations using Python's built-in list
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Implements stack operations using Python's built-in list
#   - Demonstrates push, pop, peek, isEmpty, and size operations
#   - Helps understand LIFO (Last In, First Out) behavior
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-16

# 🎯 Function to demonstrate stack operations
def display_stack_operations():
    stack = []

    # ➕ Push elements
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print("🧱 Stack:", stack)

    # 🔻 Pop the top element
    popped_element = stack.pop()
    print("🗑️ Pop:", popped_element)

    # 👀 Peek at the top element
    top_element = stack[-1]
    print("🎯 Peek:", top_element)

    # ❓ Check if stack is empty
    is_empty = not bool(stack)
    print("⚪ isEmpty:", is_empty)

    # 📏 Display stack size
    print("📏 Size:", len(stack))


# --- Example Execution / Test ---
if __name__ == "__main__":
    display_stack_operations()
