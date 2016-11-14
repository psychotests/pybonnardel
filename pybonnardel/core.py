#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

__version__ = '0.1'


class Bonnardel(object):
    def __init__(self, nb_choices=3, nb_rect_sol=2, nb_symb=2):
        """
        :param nb_choices: number of choices (default: 3)
        :param nb_rect_sol: number of rectangles in one solution (default: 2)
        :param nb_symb: number of symboles (default: 2)
        """
        self.nb_choices = nb_choices
        self.nb_rect_sol = nb_rect_sol
        self.nb_symb = nb_symb

    def run(self):
        self.sequence = dict()
        self.choices = [dict() for seq in range(self.nb_choices)]
        self.sol = -1

        for i in range(self.nb_symb):
            # generate an initial sequence and a solution
            self.sequence[i], sol_pos = self.get_sequence()

            # generate possibilities
            choices_ = self.get_choices(sol_pos)  # [[pos_r0, pos_r1, …], …]

            # get the index of the solution in choices
            sol_id = choices_.index(sol_pos)
            if self.sol == -1:
                self.sol = sol_id
            else:
                # put the solution at the right position in choices
                choices_[sol_id] = choices_[self.sol]
                choices_[self.sol] = sol_pos

            # format choices as a list of sequences
            for j, seq_c in enumerate(choices_):
                self.choices[j][i] = seq_c

        self.sol += 1  # id to used count

    def get_sequence(self, nb_rect=3):
        """
        Generate a sequence of positions for one symbole with its future (solution)

        :param nb_rect: number of rectangles in the sequence (default: 3)
        :returns: a tuple with the sequence and its future (solution)
        """
        # 8 positions in the rectangle: 4 corners & 4 middles
        condition = random.randint(0, 7)
        step = random.randint(0, 7)

        # the sequence
        sequence = [(condition + step * i) % 8 for i in range(nb_rect)]
        solution = [(condition + step * i) % 8 for i in range(nb_rect, nb_rect + self.nb_rect_sol)]

        return sequence, solution

    def get_choices(self, sol):
        """
        Introduce a perturbation in the solution of the sequence for each
        choices and return them.

        :param sol: the solution to perturbe
        :returns: possibilities of solutions shuffled (list of list of positions)
        """
        choices = [sol]
        for k in range(self.nb_choices - 1):
            possibility = []
            # possibilities
            for i in sol:
                a = random.choice([-1, 1])  # sign of the pertubation
                b = random.randint(1, 7)  # perturbation

                r = (i + a * b) % 7  # a possibility in the choice
                possibility.append(r)
            choices.append(possibility)

        # shuffle choices
        random.shuffle(choices)

        return choices
