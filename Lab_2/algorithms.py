import ai_operations as ai
import numpy as np


def solve_bkt(maze: np.ndarray, xs: int, ys: int, xd: int, yd: int) -> (bool, np.ndarray):
    """
    :param maze:
    :param xs:
    :param ys:
    :param xd:
    :param yd:
    :return: Boolean and eventual solution
    """

    maze = ai.get_initial_state(maze, xs, ys)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    solution_found = False
    solution_maze = np.array(maze)

    def bkt(bkt_maze: np.ndarray, xp: int, yp: int, nr: int):
        """
        :param nr: depth of bkt
        :param bkt_maze: current bkt maze configuration
        :param xp: current position
        :param yp: current position
        :return: Boolean and eventual solution
        """
        nonlocal solution_found
        nonlocal solution_maze
        nonlocal xd
        nonlocal yd
        if solution_found:
            return
        if ai.is_final(bkt_maze, xd, yd):
            solution_maze = bkt_maze
            solution_found = True
            return
        for possible_transition in range(4):
            # print(nr, possible_transition)
            xp2 = xp + dx[possible_transition]
            yp2 = yp + dy[possible_transition]
            if ai.is_transition_valid(bkt_maze, xp2, yp2):
                # print("DA", possible_transition, nr, "xp2 = ", xp2, "yp2 = ", yp2, xp, yp)
                maze2 = ai.apply_transition(bkt_maze, xp2, yp2)
                bkt(maze2, xp2, yp2, nr+1)

    bkt(maze, xs, ys, 0)
    return solution_found, solution_maze


def solve_lee(maze: np.ndarray, xs: int, ys: int, xd: int, yd: int) -> (bool, np.ndarray):
    """
    :param maze:
    :param xs:
    :param ys:
    :param xd:
    :param yd:
    :return: Boolean and eventual solution
    """
    maze = ai.get_initial_state(maze, xs, ys)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = [[xs, ys]]
    while len(queue) > 0:
        current_position = queue.pop(0)
        xp, yp = current_position
        maze = ai.apply_transition(maze, xp, yp)
        if ai.is_final(maze, xd, yd):
            return True, maze
        for i in range(4):
            xp2 = xp + dx[i]
            yp2 = yp + dy[i]
            if ai.is_transition_valid(maze, xp2, yp2):
                queue.append([xp2, yp2])
    return False, maze


def hill_climbing(maze: np.ndarray, xs: int, ys: int, xd: int, yd: int) -> (bool, np.ndarray):
    """
    :param maze:
    :param xs:
    :param ys:
    :param xd:
    :param yd:
    :return: Boolean and eventual solution
    """
    return False
