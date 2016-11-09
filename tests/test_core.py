#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pybonnardel.core import Bonnardel


class BonnardelTest(unittest.TestCase):
    def setUp(self):
        self.quiz = Bonnardel()

    def test_get_sequence(self):
        nb_rect = 3
        self.quiz.nb_rect_sol = 2
        sequence, sol = self.quiz.get_sequence(nb_rect)

        # sizes
        self.assertEqual(len(sequence), nb_rect)
        self.assertEqual(len(sol), self.quiz.nb_rect_sol)

    def test_get_choices(self):
        nb_rect = 3
        self.quiz.nb_rect_sol = 2
        self.quiz.nb_choices = 4
        sequence, sol = self.quiz.get_sequence(nb_rect)
        choices = self.quiz.get_choices(sol)

        # sizes
        self.assertEqual(len(choices), self.quiz.nb_choices)
        # the sol is still there
        self.assertIn(sol, choices)
