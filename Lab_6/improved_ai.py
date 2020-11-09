from functions import generate_possible_states
from game_tree import GameTree
import json
import math


def mini_max(game_state: dict, level: int = 2) -> dict:
    """

    :param game_state:
    :param level:
    :return:
    """
    current_state = generate_game_tree(game_state, level, "C")
    max_value = - math.inf
    max_index = 0
    for i in range(len(current_state.children)):
        if current_state.children[i].evaluate_current_state() > max_value:
            max_value = current_state.value
            max_index = i
    return current_state.children[max_index].game_state


def generate_game_tree(game_state: dict, level: int, player: str, parent: GameTree = None) -> GameTree:
    """

    :param game_state:
    :param level:
    :param player:
    :param parent:
    :return:
    """
    if level == 0:
        return None
    possible_states = generate_possible_states(game_state, player)
    current_state = GameTree(game_state, parent=parent, player=player)
    for state in possible_states:
        child = generate_game_tree(state, level - 1, "C" if player == "H" else "H", parent=current_state)
        current_state.add_children(child)
    current_state.evaluate_current_state()
    return current_state


