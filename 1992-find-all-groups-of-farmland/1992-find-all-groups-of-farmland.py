class Solution(object):
    def solve(self, r, c, max_coordinates, land, vis):
        # Getting the dimensions of the land
        m = len(land)
        n = len(land[0])
        
        # Marking the current cell as visited
        vis[r][c] = True
        
        # Arrays to represent four possible directions: up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        # Iterating through each direction
        for i in range(4):
            nr = dr[i] + r  # New row
            nc = dc[i] + c  # New column
            
            # Checking if the new cell is within bounds, is unvisited, and is part of farmland
            if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and not vis[nr][nc]:
                # Updating the maximum row and column encountered so far
                max_coordinates[0] = max(max_coordinates[0], nr)
                max_coordinates[1] = max(max_coordinates[1], nc)
                
                # Recursively exploring the farmland
                self.solve(nr, nc, max_coordinates, land, vis)
    
    def findFarmland(self, land):
        # Getting the dimensions of the land
        m = len(land)
        n = len(land[0])
        
        # Creating a 2D array to mark visited cells
        vis = [[False] * n for _ in range(m)]
        
        # List to store the coordinates of each farmland
        ans_list = []
        
        # Iterating through each cell in the land
        for i in range(m):
            for j in range(n):
                # If the cell is unvisited and is part of farmland
                if not vis[i][j] and land[i][j] == 1:
                    max_coordinates = [i, j]  # Initialize maximum row and column
                    
                    # Recursive function to explore and mark the farmland
                    self.solve(i, j, max_coordinates, land, vis)
                    
                    # Adding the coordinates of the farmland into the result list
                    ans_list.append([i, j, max_coordinates[0], max_coordinates[1]])
        
        return ans_list