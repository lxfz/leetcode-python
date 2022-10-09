# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        next = head.next
        
        while next != None:
            if next.val != cur.val:
                cur.next = next
                cur = cur.next
            next = next.next
        cur.next = None
        
        return head
        