class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if head is None:
            return head
        pre = head
        p = head
        q = p.next

        if q:
            p.next = q.next
            q.next = p
            pre = p
            head = q
            p = p.next
            if p:
                q = p.next
        while p and q:
            p.next = q.next
            q.next = p
            pre.next = q
            pre = p
            p = p.next
            if p:
                q = p.next

        return head
