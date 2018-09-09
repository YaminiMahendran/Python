
class Solution(object):
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None

        meet = None
        slow = head
        fast = head
        while( fast and fast.next ):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                meet = slow
                break
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next