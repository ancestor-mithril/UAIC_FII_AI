import ai_operations as ai
import numpy as np
import random
import math


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


def get_estimated_distance(current_x: int, current_y: int, destination_x: int, destination_y: int) -> int:
    """
    Calculates the expected minimum distance in maze between current and destination point

    :param current_x:
    :param current_y:
    :param destination_x:
    :param destination_y:
    :return: value = calculating and/or underestimating distance between current and destination
    """
    return abs(current_x - destination_x) + abs(current_y - destination_y)


def solve_hill_climbing(maze: np.ndarray, xs: int, ys: int, xd: int, yd: int) -> (bool, np.ndarray):
    """
    at any possible point, hill climbing chooses one random better solution, evaluating the distance between possible
    choices and current point, never overestimating the distance. The algorithm is repeated a number of times to
    be able to escape eventual local minimums found

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
    xp, yp = (xs, ys)

    for i in range(1000):
        while True:
            current_value = get_estimated_distance(xp, yp, xd, yd)
            maze = ai.apply_transition(maze, xp, yp)
            if ai.is_final(maze, xd, yd):
                return True, maze
            possible_choices = []
            for i in range(4):
                xp2 = xp + dx[i]
                yp2 = yp + dy[i]
                if ai.is_transition_valid(maze, xp2, yp2) and get_estimated_distance(xp2, yp2, xd, yd) <= current_value:
                    possible_choices.append((xp2, yp2))
            if len(possible_choices) > 0:
                xp, yp = possible_choices[random.randint(0, len(possible_choices) - 1)]
            else:
                break
    else:
        return False, maze


def solve_simulated_annealing(maze: np.ndarray, xs: int, ys: int, xd: int, yd: int) -> (bool, np.ndarray):
    """
    at any given point, simulated annealing selects a random neighbour and if it's better, it proceeds to it,
    and even if it's not better, there's a chance that it can proceed to it. This is done for a number of iterations,
    and the probability of proceeding to a worse neighbour decreases over time.

    Current implementation needs more runs for SA on default maze to give an answer

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
    xp, yp = (xs, ys)
    iterations = 0
    temperature = 100

    def lower_temperature(current_temperature: float, current_iteration: int) -> float:
        """
        temperature varies from 100 to 1, and the function to evaluate the temperature:
        math.exp(- abs(future_value - current_value) / temperature, decreases from near 100% to 37%

        :param current_temperature:
        :param current_iteration:
        :return: temperature
        """
        if temperature <= 1:
            return 1
        return temperature - math.log2(temperature) / 10

    for i in range(100):
        while True:
            current_value = get_estimated_distance(xp, yp, xd, yd)
            maze = ai.apply_transition(maze, xp, yp)
            if ai.is_final(maze, xd, yd):
                return True, maze
            possible_choices = []
            for i in range(4):
                xp2 = xp + dx[i]
                yp2 = yp + dy[i]
                future_value = get_estimated_distance(xp2, yp2, xd, yd)
                # print(math.exp(- abs(future_value - current_value) / temperature), temperature, iterations)
                if ai.is_transition_valid(maze, xp2, yp2):
                    if future_value <= current_value:
                        possible_choices.append((xp2, yp2))
                    elif random.uniform(0, 1) < math.exp(- abs(future_value - current_value) / temperature):
                        possible_choices.append((xp2, yp2))
            if len(possible_choices) > 0:
                xp, yp = possible_choices[random.randint(0, len(possible_choices) - 1)]
            temperature = lower_temperature(temperature, iterations)
            iterations += 1
            if iterations > 20000:
                break
    else:
        return False, maze
