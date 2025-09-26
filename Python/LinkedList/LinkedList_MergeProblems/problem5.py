from merge_core import Node, merge, printAndTraverse

# Problem 5: Merge when both lists have duplicate elements
# Input: 1 -> 3 -> 5, 1 -> 2 -> 3
# Expected Output: 1 -> 1 -> 2 -> 3 -> 3 -> 5

# First Linked List
Fnode1 = Node(1)
Fnode2 = Node(3)
Fnode3 = Node(5)
Fnode1.next = Fnode2
Fnode2.next = Fnode3

# Second Linked List
Snode1 = Node(1)
Snode2 = Node(2)
Snode3 = Node(3)
Snode1.next = Snode2
Snode2.next = Snode3

if __name__ == "__main__":
    head = merge(Fnode1, Snode1)
    print("Merged List is:", end=" ")
    printAndTraverse(head)