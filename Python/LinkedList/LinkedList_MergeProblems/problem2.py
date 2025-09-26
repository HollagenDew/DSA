from merge_core import Node, merge, printAndTraverse

# Problem 2: Merge two lists where one is empty
# Input: null, 5 -> 10 -> 15
# Expected Output: 5 -> 10 -> 15

# First Linked List (empty)
Fnode1 = None

# Second Linked List
Snode1 = Node(5)
Snode2 = Node(10)
Snode3 = Node(15)
Snode1.next = Snode2
Snode2.next = Snode3

if __name__ == "__main__":
    head = merge(Fnode1, Snode1)
    print("Merged List is:", end=" ")
    printAndTraverse(head)