# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        def dp(counter, node,h):
            if not node:
                return
            
            if counter not in dic:
                dic[counter] = []
            
            dic[counter].append([node.val, h])
            
            dp(counter - 1, node.left, h + 1)
            dp(counter + 1, node.right, h + 1)
        
        dp(0,root, 0)
        sorted_dict = dict(sorted(dic.items()))
        

        # Sort the values within each list based on their second index (index 1)
        for key, value in sorted_dict.items():
            sorted_dict[key] = sorted(value, key=lambda x: x[1])

        # Create a new list containing the 0th index of the sorted values
        result_list = [[x[0] for x in value] for value in sorted_dict.values()]
        return result_list

        
        