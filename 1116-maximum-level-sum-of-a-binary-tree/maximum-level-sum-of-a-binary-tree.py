class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        level = 1
        maxSum = root.val
        maxLevel = 1
        
        while queue:
            levelSize = len(queue)
            sumValue = 0
            for _ in range(levelSize):
                node = queue.popleft()
                sumValue += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if sumValue > maxSum:
                maxSum = sumValue
                maxLevel = level
                
            level += 1
            
        return maxLevel        