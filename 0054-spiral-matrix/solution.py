class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False]*cols for _ in range(rows)]
        direction = [
            (0, 1),# go right
            (1, 0),# go down
            (0, -1),# go left
            (-1, 0)# go up
        ]
        ret = []
        
        curr_dir_idx = 0
        curr_x = 0
        curr_y = 0

        while True:
            ret.append(matrix[curr_x][curr_y])
            visited[curr_x][curr_y] = True
            # follow same direction
            next_x = curr_x + direction[curr_dir_idx%4][0]
            next_y = curr_y + direction[curr_dir_idx%4][1]
            if not (
                0 <= next_x and next_x <= rows - 1 \
                and 0 <= next_y and next_y <= cols - 1 \
                and not visited[next_x][next_y]
            ):
                # change direction if not able to follow same direction
                curr_dir_idx = (curr_dir_idx+1)%4
                next_x = curr_x + direction[curr_dir_idx%4][0]
                next_y = curr_y + direction[curr_dir_idx%4][1]

            if not (
                0 <= next_x and next_x <= rows - 1 \
                and 0 <= next_y and next_y <= cols - 1 \
                and not visited[next_x][next_y]
            ):
                break
            # move pointer if still valid following same direction
            curr_x = next_x
            curr_y = next_y
        return ret
