class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        #get two list, x values and y values
        #get value for x values, calculate the travel distance for all points to that x value
        #same for y values

        x_line = []
        y_line = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_line.append(i)
                    y_line.append(j)

        x_line = sorted(x_line)
        y_line = sorted(y_line)

        median_x = x_line[len(x_line) // 2]
        median_y = y_line[len(y_line) // 2]

        travel_x = [abs(median_x - x) for x in x_line]
        travel_y = [abs(median_y - y) for y in y_line]
        return sum(travel_x) + sum(travel_y)