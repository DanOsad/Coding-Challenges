# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0, None)
        ans = curr

        p1 = list1
        p2 = list2

        while (p1.val and p2.val):
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        for p in [p1, p2]:
            if p:
                curr.next = p
                curr = curr.next

        return ans.next

cases = [
    {
        'input': ([1, 2, 4], [1, 3, 4]),
        'solution': [1, 1, 2, 3, 4, 4]
    },
    {
        'input': ([], []),
        'solution': []
    },
    {
        'input': ([], [0]),
        'solution': [0]
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().__init__
    }
)
test_suite.run_tests()