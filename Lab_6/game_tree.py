import math
from typing import List
from functions import evaluate_state


class GameTree(object):
    def __init__(self, game_state: dict, player: str, parent: "GameTree" = None, children: List["GameTree"] = None):
        """

        :param game_state:
        :param player:
        :param parent:
        :param children:
        """
        self.player = player
        if children is None:
            children = []
        self.game_state = game_state
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children
        self.value = 0

    def add_children(self, child: "GameTree"):
        """

        :param child:
        :return:
        """
        if child is not None:
            self.children.append(child)

    def serialize(self):
        return {
            "game_state": self.game_state,
            "children": [x.serialize() for x in self.children],
            "player": self.player,
            "value": self.value
        }

    def evaluate_current_state(self) -> float:
        """

        :return: current_value
        """
        if len(self.children) == 0:
            self.value = evaluate_state(self.game_state)
        else:
            if self.player == "C":
                self.value = min([x.evaluate_current_state() for x in self.children])
            else:
                self.value = max([x.evaluate_current_state() for x in self.children])

        return self.value

    def alpha_beta_pruning(self, alpha: float, beta: float) -> float:
        """

        :param alpha:
        :param beta:
        :return:
        """
        self.value = math.inf if self.player == "C" else - math.inf
        if len(self.children) == 0:
            self.value = evaluate_state(self.game_state)
            if self.player == "C":
                if self.parent.value > self.value:
                    self.parent.value = self.value
            else:
                if self.parent.value < self.value:
                    self.parent.value = self.value
