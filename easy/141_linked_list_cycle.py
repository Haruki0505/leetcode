class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def hasCycle(self, head):
  #   seen = set()
  #   while head:
  #     if head in seen:
  #       return True
  #     seen.add(head)
  #     head = head.next
  #   return False

    if not head:
      return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# links = ListNode(3)
# links.next = ListNode(2)
# links.next.next = ListNode(0)
# links.next.next.next = ListNode(-4)
# links.next.next.next.next = links.next

links = ListNode(1)
links.next = ListNode(2)
links.next.next = links

obj = Solution()
print(obj.hasCycle(links))