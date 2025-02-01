from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current and current.next:
            if current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next

# [1,2,3,3,4,4,5]
links = ListNode(1)
links.next = ListNode(2)
links.next.next = ListNode(3)
links.next.next.next = ListNode(3)
links.next.next.next.next = ListNode(4)
links.next.next.next.next.next = ListNode(4)
links.next.next.next.next.next.next = ListNode(5)

obj = Solution()
result = obj.deleteDuplicates(links)
print(result.val)