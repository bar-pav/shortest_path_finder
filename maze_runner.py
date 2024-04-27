import queue
import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
START = "X"
END = "O"

maze_template = [
    ['#', 'X', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'O', '#'],
]


def print_maze(maze, path):
    print(f"{CLEAR_AND_RETURN}{CLEAR}", end="")
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                print(f"{'.':3s}", end="")
            else:
                print(f"{value:3s}", end="")
        print()


def find_start_end(maze, start, end):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                start = i, j
            if value == end:
                end = i, j
    return start, end


def find_neighbours(position, maze):
    i, j = position
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < len(maze):
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < len(maze[0]):
        neighbours.append((i, j + 1))
    return neighbours


def find_route(maze):
    start, end = find_start_end(maze, START, END)
    q = queue.Queue()
    visited = set()
    q.put((start, [start]))
    while not q.empty():
        current, path = q.get()
        i, j = current
        print_maze(maze, path)
        time.sleep(0.3)
        if maze[i][j] == 'O':
            return path
        visited.add(current)
        neighbours = find_neighbours(current, maze)
        for neighbour in neighbours:
            i, j = neighbour
            if maze[i][j] != "#" and neighbour not in visited:
                q.put((neighbour, [*path, neighbour]))


result = find_route(maze_template)
print(result)
