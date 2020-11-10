import math
from typing import List
from functions import evaluate_state

ab_values = [math.inf if i % 2 == 1 else -math.inf for i in range(0, 5)]


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

    def alpha_beta_pruning(self, level: int) -> float:
        """

        :param level:
        :return:
        """

        if self.children:
            for child in self.children:
                child.alpha_beta_pruning(level + 1)
                if level % 2 == 1:
                    if ab_values[level] < self.value:
                        break
                elif ab_values[level] > self.value:
                    break

            if level % 2 == 1:
                if ab_values[level] > self.value:
                    ab_values[level] = self.value
                    if self.parent is not None:
                        self.parent.value = self.value
            elif ab_values[level] < self.value:
                ab_values[level] = self.value
                if self.parent is not None:
                    self.parent.value = self.value
        else:
            value = self.evaluate_current_state()
            if level % 2 == 1:
                if value > ab_values[level]:
                    self.parent.value = value
                    ab_values[level] = value
            elif value < ab_values[level]:
                self.parent.value = value
                ab_values[level] = value
