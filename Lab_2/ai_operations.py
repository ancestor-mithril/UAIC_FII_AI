
import numpy as np
import maze_creator as f


def get_problem_instance(mx: int, my: int) -> np.ndarray:
    """
    :param mx: maze dimension
    :param my: maze dimension
    :return: the maze
    """
    maze = f.create_maze(mx, my)
    return np.pad(maze, pad_width=1, mode='constant', constant_values=0)


def get_initial_state(maze: np.ndarray, xs: int, ys: int) -> np.ndarray:
    """
    :param maze: ndarray
    :param xs: x coordinate of start point
    :param ys: y coordinate of start point
    :return: a copy of the maze with the start position visited
    """
    maze2 = maze.copy()
    maze2[xs, ys] = 2
    return maze2


def is_final(maze: np.ndarray, xd: int, yd: int) -> bool:
    """
    :param maze: the maze
    :param xd: x coordinate of start position
    :param yd: y coordinate of start position
    :return: True, if maze[xd, yd] is 2, False otherwise
    """
    return maze[xd, yd] == 2


def is_transition_valid(maze: np.ndarray, xt: int, yt: int) -> bool:
    """
    :param maze: the maze
    :param xt: x coordinate of wanted transition
    :param yt: y coordinate of wanted transitiom
    :return: True, if maze[xt, yt] is 1, False otherwise
    """
    return maze[xt, yt] == 1


def apply_transition(maze: np.ndarray, xt: int, yt: int) -> np.ndarray:
    """
    :param maze: the maze
    :param xt: x coordinate of wanted transition
    :param yt: y coordinate of wanted transitiom
    :return: a copy of the maze after transition
    """
    maze2 = maze.copy()
    maze2[xt, yt] = 2
    return maze2
