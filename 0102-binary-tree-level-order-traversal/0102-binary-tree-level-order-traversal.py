# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = collections.deque()

        # we start's with the root node which also means that we visited the 0th level so add it in the queue
        if root:
            queue.append(root)

        while queue:

            levelArray = []

            for i in range(len(queue)):

                current_node = queue.popleft()

                levelArray.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
            res.append(levelArray)
        return res