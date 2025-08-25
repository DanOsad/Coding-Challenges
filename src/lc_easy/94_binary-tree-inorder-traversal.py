# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
        # Definition for a binary tree node.
        # class TreeNode(object):
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            visited.append(root.val)
            traverse(root.right)

        traverse(root)
        return visited


cases = [
    {
        'input': [1,None,2,3],
        'solution': [1, 3, 2]
    },
    {
        'input': [1,2,3,4,5,None,8,None,None,6,7,9],
        'solution': [4, 2, 6, 5, 7, 1, 3, 9, 8]
    },
    {
        'input': [],
        'solution': []
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