class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        ans = []
        
        
        for idx, char in enumerate(searchWord):

            temp = []
            j = 0
            for p in products:
                if p[:idx + 1] == searchWord[:idx + 1]:
                    temp.append(p)
                    j += 1
            ans.append(temp[:3])
            products = temp
        return ans
        