from mesa import Agent
import random
from itertools import combinations


class Agent(Agent):
    def __init__(self, unique_id, model):
        """
        Play explanation:
        1 - paper (red), 2 - rock (grey), 3 - scissors (cyan)
            1 beats 2 but loses to 3
            2 beats 3 but loses to 1
            3 beats 1 but loses to 2

        Score is the running total of the agents success.
        """
        super().__init__(unique_id, model)
        # FIXME: the play should be based on the strategy
        self.score = 0
        self.strategy = random.choice(["Pure Rock", "Pure Paper", "Pure Scissors", "Perfect Mixed"])
        # self.play = random.choice("Rock", "Paper", "Scissors")
        self.neighbours = []
        self.play = ""

    def combinations(self):
        for combo in combinations([1, 2, 3], 2):
            pass
            # output is (1, 2), (1, 3), (2, 3)

    def rock_paper_scissors(self, neighbour):
        # TODO: Should be able to shorten code using combinatorics
        # FIXME: the current sum of scores is non-zero
        if self.play == "Paper":
            if neighbour.play == "Rock":
                self.score += 1
            elif neighbour.play == "Scissors":
                self.score -= 1
        elif self.play == "Rock":
            if neighbour.play == "Paper":
                self.score -= 1
            elif neighbour.play == "Scissors":
                self.score += 1
        elif self.play == "Scissors":
            if neighbour.play == "Paper":
                self.score += 1
            elif neighbour.play == "Rock":
                self.score -= 1

    def calculate_scores(self):
        """
        Plays x rounds between agents of the game.
        :return: score of the agents
        """

        self.neighbours =\
            self.model.grid.get_neighbors(
                pos=self.pos,
                moore=True,
                # when moore is True, diagonals are included
                include_center=False)
        for neighbour in self.neighbours:
            # the pure strategies have the plays remaining unchanged so go outside the for loop
            if self.strategy == "Pure Rock":
                self.play = "Rock"
            elif self.strategy == "Pure Paper":
                self.play = "Paper"
            elif self.strategy == "Pure Scissors":
                self.play = "Scissors"
            for _ in range(self.model.num_plays_per_set):
                if self.strategy == "Perfect Mixed":
                    self.play = random.choice(["Rock", "Paper", "Scissors"])
                self.rock_paper_scissors(neighbour)
                # self.evolution.evolve.mutate()

    def step(self):
        self.calculate_scores()
