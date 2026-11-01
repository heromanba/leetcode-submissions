from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.w = width
        self.h = height
        self.food = food
        self.score = 0
        self.on_snake = { (0,0) }
        self.snake = deque([(0,0)])
        self.deltas = {
            'U': (-1,0),
            'D': (1,0),
            'L': (0,-1),
            'R': (0, 1),
        }


    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[0]
        delta_row, delta_col = self.deltas[direction]
        next_head = (head_row+delta_row, head_col+delta_col)

        if next_head[0] < 0 or next_head[0] >= self.h or \
            next_head[1] < 0 or next_head[1] >= self.w:
            # cross the boarder
            return -1

        if self.score < len(self.food) and next_head == tuple(self.food[self.score]):
            # increase score and do not move tail
            self.score += 1
        else:
            # no score change and move the tail
            tail = self.snake.pop()
            self.on_snake.remove(tail)

        if next_head in self.on_snake:
            # collide with self
            return -1

        self.on_snake.add(next_head)
        self.snake.appendleft(next_head)

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
