
import numpy as np
import random


def get_problem_instance_2(mx: int, my: int) -> (np.ndarray, (int, int), (int, int)):
    """
    :param mx: length of maze
    :param my: height of maze
    :return: maze, Start point, Destination point
    """
    while True:
        maze = f.create_maze(mx, my)
        # maze_2 = np.random.randint(0, 2, size=(10, 10))  # creaza o matrice de 0 si 1 random cu distributia 50-50
        # maze_2 = np.random.choice(2, size=(mx, my), p=[0.2, 0.8])
        # creaza o matrice de 0 si 1 random cu distributia  0.2 - 0.8
        maze = np.pad(maze, pad_width=1, mode='constant', constant_values=0)
        xs = random.randint(0, mx - 1)
        ys = random.randint(0, my - 1)
        xd = random.randint(0, mx - 1)
        yd = random.randint(0, my - 1)
        if maze[xs, ys] == 1 and maze[xd, yd] == 1:
            return maze, (xs, ys), (xd, yd)

def is_final(maze: np.ndarray, xd: int, yd: int) -> bool:
    """
    :param maze: the maze
    :param xd: x coordinate of start position
    :param yd: y coordinate of start position
    :return: True, if maze[xd, yd] is 2, False otherwise
    """
    # f.write(str(maze) + ' is final maze\n' + str((xd, yd)) +
    #         ' xd, yd is final maze\n' + str(maze[xd, yd] == 2) + ' maze[xd, yd] == 2\n')
    # print(maze, 'is final maze\n', xd, yd, 'xd, yd is final maze\n', maze[xd, yd] == 2, 'maze[xd, yd] == 2\n')
    return maze[xd, yd] == 2