class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        front = rear = pre = head
        i = 1
        next_p = head
        while next_p:
            # Move to the pointer to be inserted
            while i < k and rear:
                rear = rear.next
                i += 1
            if i != k or not rear:
                break
            elif pre == head:
                head = rear
            else:
                # link list after swap
                pre.next = rear

            pre = front
            next_p = rear.next

            while front != rear:
                temp = front.next
                front.next = rear.next
                rear.next = front
                front = temp
            front = rear = next_p
            i = 1

        return head
