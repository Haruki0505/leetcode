from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        carry_up = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + carry_up
            carry_up = value // 10

            current.next = ListNode(value % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        if carry_up != 0:
            current.next = ListNode(carry_up)

        return dummy.next

# links_1 = ListNode(2)
# links_1.next = ListNode(4)
# links_1.next.next = ListNode(3)

# links_2 = ListNode(5)
# links_2.next = ListNode(6)
# links_2.next.next = ListNode(4)

# links_1 = ListNode(0)

# links_2 = ListNode(0)

# links_1 = ListNode(9)
# links_1.next = ListNode(9)
# links_1.next.next = ListNode(9)
# links_1.next.next.next = ListNode(9)
# links_1.next.next.next.next = ListNode(9)
# links_1.next.next.next.next.next = ListNode(9)
# links_1.next.next.next.next.next.next = ListNode(9)

# links_2 = ListNode(9)
# links_2.next = ListNode(9)
# links_2.next.next = ListNode(9)
# links_2.next.next.next = ListNode(9)

links_1 = ListNode(2)
links_1.next = ListNode(4)
links_1.next.next = ListNode(9)

links_2 = ListNode(5)
links_2.next = ListNode(6)
links_2.next.next = ListNode(4)
links_2.next.next.next = ListNode(9)

def printList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

obj = Solution()
result = obj.addTwoNumbers(links_1, links_2)
print(printList(result))