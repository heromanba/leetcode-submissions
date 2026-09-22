class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [ [-1]*n for _ in range(n) ]
        directions = [
            (0, 1), # go right
            (1, 0), # go down
            (0, -1), # go left
            (-1, 0), # go up
        ]
        curr_dir_idx = 0
        curr_x = 0
        curr_y = 0

        for i in range(1,n*n+1):
            matrix[curr_x][curr_y] = i
            # not able to follows same direction
            next_x = curr_x + directions[ curr_dir_idx%4 ][0]
            next_y = curr_y + directions[ curr_dir_idx%4 ][1]
            if not (
                0 <= next_x and next_x < n and\
                0 <= next_y and next_y < n and\
                matrix[next_x][next_y] == -1
            ):
                # change direction
                curr_dir_idx += 1
                
                next_x = curr_x + directions[ curr_dir_idx%4 ][0]
                next_y = curr_y + directions[ curr_dir_idx%4 ][1]

                # still not able to move then return
                if not (
                    0 <= next_x and next_x < n and\
                    0 <= next_y and next_y < n and\
                    matrix[next_x][next_y] == -1
                ):
                    return matrix

            curr_x = next_x
            curr_y = next_y
        return matrix
