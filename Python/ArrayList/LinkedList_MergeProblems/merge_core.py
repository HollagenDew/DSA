from typing import Optional

class Node:
    """
    Class representing a single node in a linked list.
    - data: stores the value of the node
    - next: points to the next node (default = None)
    """
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


def printAndTraverse(head: Optional[Node]) -> None:
    """
    Traverse the linked list and print all node values.
    Format: value -> value -> ... -> null
    """
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def merge(left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted linked lists into one sorted list.
    Re-links existing nodes instead of creating new ones.
    
    Args:
        left: Head node of the first linked list
        right: Head node of the second linked list
    
    Returns:
        Head node of the merged sorted linked list
    """
    # Handle cases where one list is empty
    if left is None:
        return right
    if right is None:
        return left

    # Dummy node to simplify edge cases
    dummy = Node(0)
    tail = dummy

    # Merge nodes one by one
    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    # Append remaining nodes
    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next