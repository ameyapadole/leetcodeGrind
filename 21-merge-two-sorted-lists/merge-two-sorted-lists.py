# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None:
            return l2
        
        elif l2 is None:
            return l1
        
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

        #Time = O(m + m)
        # Because each recursive call increments the pointer l1 or l2 by 1.
        # There will be exactly one call to mergeTwoLists per element in each list.
        # Hence the Time complexit is liner in the combined size of the lists.

        #Space = O(n + m)
        # The first call does not return until both l1 and l2 have been reached, so n + m stack frames consumes n + m Space.
