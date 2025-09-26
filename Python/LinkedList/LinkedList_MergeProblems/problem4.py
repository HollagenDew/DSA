from merge_core import Node, merge, printAndTraverse

# Problem 4: Merge two lists of different lengths
# Input: 1 -> 5 -> 7 -> 9, 2 -> 4
# Expected Output: 1 -> 2 -> 4 -> 5 -> 7 -> 9

# First Linked List
Fnode1 = Node(1)
Fnode2 = Node(5)
Fnode3 = Node(7)
Fnode4 = Node(9)
Fnode1.next = Fnode2
Fnode2.next = Fnode3
Fnode3.next = Fnode4

# Second Linked List
Snode1 = Node(2)
Snode2 = Node(4)
Snode1.next = Snode2

if __name__ == "__main__":
    head = merge(Fnode1, Snode1)
    print("Merged List is:", end=" ")
    printAndTraverse(head)