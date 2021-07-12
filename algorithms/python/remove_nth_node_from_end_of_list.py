# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create two pointers
        back = front = head

        # Create a delay = n between the pointers
        for _ in range(n):
            if front.next is not None:
                front = front.next
            else:
                # delay = length of the list
                # The node we are removing is the head
                return head.next

        # Move back to the node before the node we are removing
        while front.next is not None:
            back = back.next
            front = front.next

        # Remove the nth node from the end of list
        back.next = back.next.next

        return head