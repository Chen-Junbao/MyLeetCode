from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        p = head = ListNode(0)
        queue = PriorityQueue()
        index = 0       # Prevent TypeError during PriorityQueue comparison

        for list in lists:
            if list:
                queue.put((list.val, index, list))
                index += 1

        while not queue.empty():
            val, index, node = queue.get()
            p.next = node
            p = p.next
            node = node.next
            if node:
                queue.put((node.val, index, node))
                index += 1

        return head.next
