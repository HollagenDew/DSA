from merge_core import Node, merge, printAndTraverse

# Problem 1: Merge two sorted linked lists
# Input: 1 -> 4 -> 7, 2 -> 3 -> 6
# Expected Output: 1 -> 2 -> 3 -> 4 -> 6 -> 7

# First Linked List
Fnode1 = Node(1)
Fnode2 = Node(4)
Fnode3 = Node(7)
Fnode1.next = Fnode2
Fnode2.next = Fnode3

# Second Linked List
Snode1 = Node(2)
Snode2 = Node(3)
Snode3 = Node(6)
Snode1.next = Snode2
Snode2.next = Snode3

if __name__ == "__main__":
    head = merge(Fnode1, Snode1)
    print("Merged List is:", end=" ")
    printAndTraverse(head)