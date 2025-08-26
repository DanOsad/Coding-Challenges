# https://leetcode.com/problems/same-tree/
class Solution:
        # Definition for a binary tree node.
        # class TreeNode(object):
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Base Cases:
        # 1) If both nodes are null = True
        if not p and not q:
            return True
        # 2) If either p or q is null OR their values are different = False
        if (not p or not q) or (p.val != q.val):
            return False
        
        is_left_tree_same = self.isSameTree(p.left, q.left)
        is_right_tree_same = self.isSameTree(p.right, q.right)

        return is_left_tree_same and is_right_tree_same


cases = [
    {
        'input': 'p = [1,2,3], q = [1,2,3]',
        'solution': True
    },
    {
        'input': 'p = [1,2], q = [1,null,2]',
        'solution': False
    },
    {
        'input': 'p = [1,2,1], q = [1,1,2]',
        'solution': False
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