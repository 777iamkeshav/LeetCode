class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = []
        result = 0
        def dfsmap(node, prefixMap, prefix):
            if not node:
                return

            nonlocal result
            prefix += node.val

            if prefix - targetSum in prefixMap:
                result += prefixMap[prefix - targetSum]
            if prefix in prefixMap:
                prefixMap[prefix] += 1
            else:
                prefixMap[prefix] = 1 

            if node.left:
                dfsmap(node.left, prefixMap.copy(), prefix)
            if node.right:
                dfsmap(node.right, prefixMap.copy(), prefix)
        
        dfsmap(root, {0:1}, 0)
        
        return result      