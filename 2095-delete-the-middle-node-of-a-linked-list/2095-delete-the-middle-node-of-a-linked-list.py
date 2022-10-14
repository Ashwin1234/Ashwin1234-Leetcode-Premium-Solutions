# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0
        count = 1
        while(cur!=None):
            n = n + 1
            cur = cur.next
        if n == 1:
            return None
        mid = int(n/2)
        cur = head
        while(count < mid):
            cur = cur.next
            count = count + 1
        fast = cur.next
        cur.next = fast.next
        return head
        