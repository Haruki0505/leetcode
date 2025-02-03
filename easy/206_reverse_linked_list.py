from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, current = None, head

        # while current:
        #     temp_next = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp_next

        # return prev

        if not head:
           return None

        stack = []
        while head.next:
            stack.append(head)
            head = head.next

        while stack:
            cur = stack.pop()
            cur.next.next = cur
            cur.next = None

        return head

linked_list = ListNode(1)
linked_list.next = ListNode(2)
linked_list.next.next = ListNode(3)
linked_list.next.next.next = ListNode(4)
linked_list.next.next.next.next = ListNode(5)

obj = Solution()
print(obj.reverseList(linked_list).val)