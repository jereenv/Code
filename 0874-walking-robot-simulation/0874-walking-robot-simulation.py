class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        
        turns = {-1, -2}
        
        direction = 0
        obstacles = {(x, y) for x, y in obstacles}
        
        
        m = 0
        
        for command in commands:
            if command in turns:
                direction = (direction + (1 if command == -1 else -1))%4
            else:
                if direction == 0:
                    while command:
                        if (x, y + 1) in obstacles:
                            break
                        y += 1
                        command -= 1
                elif direction == 1:
                    while command:
                        if (x + 1, y) in obstacles:
                            break
                        x += 1
                        command -= 1
                elif direction == 2:
                    while command:
                        if (x, y - 1) in obstacles:
                            break
                        y -= 1
                        command -= 1
                else:
                    while command:
                        if (x - 1, y) in obstacles:
                            break
                        x -= 1
                        command -= 1
                m = max(m, x**2+ y**2)
        
        return m