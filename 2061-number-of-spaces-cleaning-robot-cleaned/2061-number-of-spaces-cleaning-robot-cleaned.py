class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])

        if not ((m > 1 and room[1][0] == 0) or (n > 1 and room[0][1] == 0)):
            return 1

        directions = (0, 1), (1, 0), (0, -1), (-1, 0)  # order matters
        cleaned = dict()  # {(row, col): direction}
        r = c = d = 0  # row, col, direction

        while True:
            if (r, c) in cleaned and cleaned[(r, c)] == d:
                break
            if (r, c) not in cleaned:
                cleaned[(r, c)] = d
            nr, nc = r + directions[d][0], c + directions[d][1]
            while nr < 0 or nr >= m or nc < 0 or nc >= n or room[nr][nc]:
                d = (d + 1) % 4
                nr, nc = r + directions[d][0], c + directions[d][1]
            r, c = nr, nc

        return len(cleaned)