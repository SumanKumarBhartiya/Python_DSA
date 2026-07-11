# Q. Write a Python program to reverse a linked list.

# Ans. Reverse a singly linked list in Python.

    # -- Approach
    # Initialize three pointers: previous as None, current as head, and next as None.
    # Iterate through the linked list until current is None.
    # In each iteration, store current's next node, reverse current's next pointer to 
    # previous, then move previous and current forward.
    # Return previous as the new head of the reversed list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev