# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        string = ""
        cur = head
        while(cur!=None):
            arr.append(cur.val)
            cur = cur.next
        for ele in arr:
            string = string + str(ele)
        return int(string,2)