class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        p = l1
        q = l2
        l3 = ListNode(0)
        r = l3
        s = r
        while p is not None and q is not None:
            dig_1 = int((p.val + q.val + r.val) % 10)
            dig_2 = int((p.val + q.val + r.val) / 10)
            r.val = dig_1
            if dig_2 != 0:
                r.next = ListNode(dig_2)
            else:
                r.next = ListNode(0)

            p = p.next
            q = q.next
            s = r
            r = r.next

        while p is not None:
            dig_1 = int((p.val + r.val) % 10)
            dig_2 = int((p.val + r.val) / 10)
            r.val = dig_1
            if dig_2 != 0:
                r.next = ListNode(dig_2)
            else:
                r.next = ListNode(0)

            p = p.next
            s = r
            r = r.next
        while q is not None:
            dig_1 = int((q.val + r.val) % 10)
            dig_2 = int((q.val + r.val) / 10)
            r.val = dig_1
            if dig_2 != 0:
                r.next = ListNode(dig_2)
            else:
                r.next = ListNode(0)

            q = q.next
            s = r
            r = r.next

        if r.val == 0:
            s.next = None

        return l3
