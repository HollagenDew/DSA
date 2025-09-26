from merge_core import Node, merge, printAndTraverse

# Problem 3: Merge two lists where all elements of one are smaller
# Input: 1 -> 2 -> 3, 10 -> 20 -> 30
# Expected Output: 1 -> 2 -> 3 -> 10 -> 20 -> 30

# First Linked List
Fnode1 = Node(1)
Fnode2 = Node(2)
Fnode3 = Node(3)
Fnode1.next = Fnode2
Fnode2.next = Fnode3

# Second Linked List
Snode1 = Node(10)
Snode2 = Node(20)
Snode3 = Node(30)
Snode1.next = Snode2
Snode2.next = Snode3

if __name__ == "__main__":
    head = merge(Fnode1, Snode1)
    print("Merged List is:", end=" ")
    printAndTraverse(head)