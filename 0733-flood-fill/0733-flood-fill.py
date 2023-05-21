class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        maxR = len(image)
        maxC = len(image[0])
        srC = image[sr][sc]

        def dfs(r,c):
            if srC == color:
                return
            if r < 0 or r >= maxR:
                return
            if c<0 or c>= maxC:
                return
            
            if image[r][c] == srC:
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        dfs(sr,sc)
        return image
            
        