class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        node_array = []
        p = head
        while p is not None:
            node_array.append(p)
            p = p.next
        length = len(node_array)
        if length == 1 and n == 1:
            return None

        index = length - n - 1
        if index == -1:
            # delete head
            return node_array[1]

        node_array[index].next = node_array[index].next.next

        return head
