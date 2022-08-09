# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        sp,fp=head,head.next
        while fp and fp.next:
            if sp==fp:
                return True
            sp=sp.next
            fp=fp.next.next
        return False