# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Base case: either lists are exhausted
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        else:
            root = ListNode()
            if l1.val <= l2.val:
                root.val = l1.val
                root.next = self.mergeTwoLists(l1.next, l2)
            else:
                root.val = l2.val
                root.next = self.mergeTwoLists(l1, l2.next)
            return root