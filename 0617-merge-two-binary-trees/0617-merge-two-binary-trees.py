class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        newTree = TreeNode(0,None,None)
        
        def merge(node1,node2,node3):
            if node1 != None:
                node3.val += node1.val
            if node2 != None:
                node3.val += node2.val
            
            if node1 == None:
                if node2 == None:
                    node3 = None
                else:
                    node3.left = node2.left
                    node3.right = node2.right
            else:
                if node2 == None:
                    node3.left = node1.left
                    node3.right = node1.right
                else:
                    node3.left = merge(node1.left,node2.left,TreeNode(0,None,None))
                    node3.right = merge(node1.right,node2.right,TreeNode(0,None,None))
            return node3

        return merge(root1,root2,newTree)

        # newTree = TreeNode(0,None,None)

        # def merge(node1,node2,node3):

        #     if node1 != None:
        #         node3.val += node1.val
            
        #     if node2 != None:
        #         node3.val += node2.val

        #     if node1 == None and node2 != None:
        #         node3.left = node2.left
        #         node3.right = node2.right
        #         return node3
        #     elif node1 != None and node2 == None:
        #         node3.left = node1.left
        #         node3.right = node1.right
        #         return node3      

        #     elif node1 == None and node2 == None:
        #         return None
        #     else:
        #         node3.left = merge(node1.left,node2.left,TreeNode(0,None,None))
        #         node3.right = merge(node1.right,node2.right,TreeNode(0,None,None))
        #         return node3

        # return merge(root1,root2,newTree)

