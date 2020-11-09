from __future__ import print_function
import json
import numpy as np
import sys

def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_initial_state() -> dict:
    """

    :return: dictionary with each piece coordinates for each player
    """
    return {
        "H": [[0, 0], [0, 1], [0, 2], [0, 3]],
        "C": [[3, 0], [3, 1], [3, 2], [3, 3]]
    }


def check_final_state(game_state: dict) -> (bool, str):
    """

    :param game_state: game dictionary containing pieces position
    :return: True, winner if winning condition, False, None otherwise
    """
    if False not in [False if i[0] != 3 else True for i in game_state["H"]]:
        return True, "H"
    if False not in [False if i[0] != 0 else True for i in game_state["C"]]:
        return True, "C"
    return False, None


def is_valid(game_state: dict, transition: list) -> bool:
    """

    :param game_state: a state
    :param transition: the transition to be made
    :return: True if transition is possible, false otherwise
    """
    if 0 <= transition[0] <= 3 and 0 <= transition[1] <= 3:
        return transition not in game_state["C"] and transition not in game_state["H"]
    return False


def generate_possible_states(game_state: dict, current_player: str) -> list:
    """

    :param current_player: may be "C" or "H"
    :param game_state: dictionary of current position
    :return: all possible future positions for calculator
    """
    assert current_player == "C" or current_player == "H"
    possible_states = []
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for index, p in enumerate(game_state[current_player]):
        for i, j in zip(dx, dy):
            transition = [p[0] + i, p[1] + j]
            if is_valid(game_state, transition):
                possible_state = json.loads(json.dumps(game_state))
                possible_state[current_player][index] = transition
                possible_states.append(possible_state)
    return possible_states


def evaluate_state(state: dict) -> int:
    """

    :param state: current state dictionary of positions
    :return: value of state
    """
    return 12 - sum([x[0] for x in state["C"]]) - sum([x[0] for x in state["H"]])


def evaluate_player_state(state: dict) -> int:
    """

    :param state: current state dictionary of positions
    :return: value of state, for player
    """
    return 12 - sum([3 - x[0] for x in state["C"]]) - sum([3 - x[0] for x in state["H"]])


def generate_best_state(game_state: dict) -> dict:
    """
    evaluates all possible future states

    :param game_state: current state dictionary of positions
    :return: best state chosen with evaluate_state() heuristic
    """
    max_value = 0
    max_index = 0
    state_list = generate_possible_states(game_state, "C")
    for index, state in enumerate(state_list):
        # state = generate_player_best_state(state)
        state_value = evaluate_state(state)
        if state_value > max_value:
            max_value = state_value
            max_index = index
    print("valoare euristica maxima: ", max_value)
    return state_list[max_index]


def to_string(game_state: dict) -> np.ndarray:
    """
    transforms the game state to a matrix

    :param game_state: dictionary of pieces positions
    :return: np nd array with each pieces position
    """
    game_matrix = np.zeros((4, 4))
    for i in game_state["C"]:
        game_matrix[i[0], i[1]] = 2
    for i in game_state["H"]:
        game_matrix[i[0], i[1]] = 1
    return game_matrix


def validate_player_choice(game_state: dict, chosen_piece: list) -> bool:
    """

    :param game_state: dictionary of current positions
    :param chosen_piece: list of piece coordinates chosen by player
    :return: True, if piece exists, False otherwise
    """
    return chosen_piece in game_state["H"]


def generate_piece_transitions(game_state: dict, chosen_piece: list) -> list:
    """

    :param game_state: dictionary of current positions
    :param chosen_piece: validated before piece coordinates
    :return: all possible future and valid positions of chosen_piece
    """
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    possible_positions = []
    for i, j in zip(dx, dy):
        transition = [chosen_piece[0] + i, chosen_piece[1] + j]
        if is_valid(game_state, transition):
            possible_positions.append(transition)
    return possible_positions


def validate_player_move(game_state: dict, chosen_piece: list, future_position: list) -> bool:
    """

    :param game_state: dictionary of current positions
    :param chosen_piece: validated before piece coordinates
    :param future_position: unvalidated future position
    :return: True if future position is valid, False otherwise
    """
    return future_position in generate_piece_transitions(game_state, chosen_piece)


def apply_player_move(game_state: dict, chosen_piece: list, future_position: list) -> dict:
    """

    :param game_state: dictionary of current positions
    :param chosen_piece: validated before piece coordinates
    :param future_position: validated future position
    :return: game_state after player move
    """
    for index, piece in enumerate(game_state["H"]):
        if piece == chosen_piece:
            game_state["H"][index] = future_position
            return game_state
    raise EnvironmentError("Nu sunt valide piesele validate")


