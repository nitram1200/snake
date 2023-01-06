from pathfinding import width, height
import numpy

print(width, height)

snake_list = [[500, 400], [400, 400], [300, 400], [200, 400], [100, 400], [0, 400]]
food = [1200, 300]
snake_size = 100


snake = []
print(snake_size)

for x in snake_list:
    snake.append([x[0] // snake_size, x[1] // snake_size])


grid = numpy.zeros((round(width / snake_size), round(height / snake_size)), dtype=numpy.int8)
print(grid.shape)

for x in snake:
    grid[x[0], x[1]] = 1

grid[food[0] // snake_size, food[1] // snake_size] = 5
grid[snake[-1][0], snake[-1][1]] = 2
print(grid)
