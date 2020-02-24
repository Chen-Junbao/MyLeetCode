class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        p = l1
        q = l2
        l3 = ListNode(0)
        r = l3
        while p is not None and q is not None:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next

        while p is not None:
            r.next = p
            p = p.next
            r = r.next
        while q is not None:
            r.next = q
            q = q.next
            r = r.next

        return l3.next
