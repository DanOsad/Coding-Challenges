# 102 https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root) -> list:
        queue = [root]
        answer = []

        if root is None:
            return answer
        
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            answer.append(level)

        return answer
        