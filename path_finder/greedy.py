from model.model import IMaze


def greedy(start_x, start_y, end_x, end_y, maze: IMaze):
    current_x = start_x
    current_y = start_y
    path = [[current_x, current_y]]

    shortest_path = [[0 for x in range(maze.get_width())] for y in range(maze.get_height())]
    for x in range(maze.get_width()):
        for y in range(maze.get_height()):
            shortest_path[x][y] = abs(end_x - x) + abs(end_y - y)

    while current_x != end_x and current_y != end_y:
        shortest = shortest_path[current_x + 1][current_y]
        shortest_x = current_x + 1
        shortest_y = current_y

        if shortest_path[current_x - 1][current_y] < shortest:
            shortest = shortest_path[current_x - 1][current_y]
            shortest_x = current_x - 1
            shortest_y = current_y

        if shortest_path[current_x][current_y + 1] < shortest:
            shortest = shortest_path[current_x][current_y + 1]
            shortest_x = current_x
            shortest_y = current_y + 1

        if shortest_path[current_x][current_y - 1] < shortest:
            shortest_x = current_x
            shortest_y = current_y - 1

        current_x = shortest_x
        current_y = shortest_y

        path.append([current_x, current_y])

    return path
