from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # seenNodes = set()

        # while head:
        #     if head in seenNodes:
        #         return head
        #     seenNodes.add(head)
        #     head = head.next
        # return None

        if head is None or head.next is None:
            return None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
                return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

links = ListNode(3)
links.next = ListNode(2)
links.next.next = ListNode(0)
links.next.next.next = ListNode(-4)
links.next.next.next.next = links.next

obj = Solution()
print(obj.detectCycle(links))