# https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # The idea here is to create a dummy node which
        # you always insert the next node as it's 'next'
        # and reverse the links, finally returning the 
        # new head, which is the dummy's 'next'
        curr = head
        dummy = ListNode()

        while curr != None:
            next = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = next

        return dummy.next