# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr_node = head
        while curr_node:
            while curr_node.next and curr_node.next.val == curr_node.val:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        return head


cases = [
    {
        'input': [1,1,2],
        'solution': [1, 2]
    },
    {
        'input': [1,1,2,3,3],
        'solution': [1, 2, 3]
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().deleteDuplicates
    }
)
test_suite.run_tests()