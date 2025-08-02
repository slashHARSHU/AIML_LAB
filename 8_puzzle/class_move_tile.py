# ==================================================================
# File: class_move_tile.py
#
# This file implements the functionality to move the empty tile
# in the 8-puzzle problem. It provides a function to generate new
# states by moving the empty tile in all possible directions.
#
# Author: Harshad Gaikwad
# Affiliation: COEP Technical University, Pune
#
# NOTE: This code is distributed strictly for educational purposes.
# It is not intended for commercial use or distribution.
# ==================================================================
import numpy as np


class MoveTile:
    """
    Class to handle the movement of the empty tile in the 8-puzzle problem.
    """

    @staticmethod
    def move_empty_tile(temp_state):
        new_possibilities = np.empty((0, 3, 3), dtype=int)

        # -------------------------------------------------------------------
        # for corner moves
        # -------------------------------------------------------------------
        # if -1 is at top left corner-------------------------
        if temp_state[0, 0] == -1:
            # to get two possibilities
            new_state0 = temp_state.copy()  # for right move
            new_state1 = temp_state.copy()  # for down move

            # perform right move
            new_state0[0, 0] = new_state0[0, 1]
            new_state0[0, 1] = -1

            # perform down move
            new_state1[0, 0] = new_state1[1, 0]
            new_state1[1, 0] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3)], axis=0)

        # if -1 is at top right corner--------------------------
        if temp_state[0, 2] == -1:
            # to get two possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for down move

            # perform left move
            new_state0[0, 2] = new_state0[0, 1]
            new_state0[0, 1] = -1

            # perform down move
            new_state1[0, 2] = new_state1[1, 2]
            new_state1[1, 2] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3)], axis=0)

        # if -1 is at bottom left corner-------------------------
        if temp_state[2, 0] == -1:
            # to get two possibilities
            new_state0 = temp_state.copy()  # for right move
            new_state1 = temp_state.copy()  # for up move

            # perform right move
            new_state0[2, 0] = new_state0[2, 1]
            new_state0[2, 1] = -1

            # perform up move
            new_state1[2, 0] = new_state1[1, 0]
            new_state1[1, 0] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3)], axis=0)

        # if -1 is at bottom right corner-------------------------
        if temp_state[2, 2] == -1:
            # to get two possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for up move

            # perform left move
            new_state0[2, 2] = new_state0[2, 1]
            new_state0[2, 1] = -1

            # perform up move
            new_state1[2, 2] = new_state1[1, 2]
            new_state1[1, 2] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3)], axis=0)

        # -------------------------------------------------------------------
        # for center moves
        # -------------------------------------------------------------------
        if temp_state[1, 1] == -1:
            # to get four possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for right move
            new_state2 = temp_state.copy()  # for up move
            new_state3 = temp_state.copy()  # for down move

            # perform left move
            new_state0[1, 1] = new_state0[1, 0]
            new_state0[1, 0] = -1

            # perform right move
            new_state1[1, 1] = new_state1[1, 2]
            new_state1[1, 2] = -1

            # perform up move
            new_state2[1, 1] = new_state2[0, 1]
            new_state2[0, 1] = -1

            # perform down move
            new_state3[1, 1] = new_state3[2, 1]
            new_state3[2, 1] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3),
                 new_state2.reshape(1, 3, 3), new_state3.reshape(1, 3, 3)], axis=0)

        # -------------------------------------------------------------------
        # for side center moves
        # -------------------------------------------------------------------
        # for left side center
        if temp_state[1, 0] == -1:
            # to get three possibilities
            new_state0 = temp_state.copy()  # for right move
            new_state1 = temp_state.copy()  # for up move
            new_state2 = temp_state.copy()  # for down move

            # perform right move
            new_state0[1, 0] = new_state0[1, 1]
            new_state0[1, 1] = -1

            # perform up move
            new_state1[1, 0] = new_state1[0, 0]
            new_state1[0, 0] = -1

            # perform down move
            new_state2[1, 0] = new_state2[2, 0]
            new_state2[2, 0] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3),
                 new_state2.reshape(1, 3, 3)], axis=0)

        # for right side center
        if temp_state[1, 2] == -1:
            # to get three possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for up move
            new_state2 = temp_state.copy()  # for down move

            # perform left move
            new_state0[1, 2] = new_state0[1, 1]
            new_state0[1, 1] = -1

            # perform up move
            new_state1[1, 2] = new_state1[0, 2]
            new_state1[0, 2] = -1

            # perform down move
            new_state2[1, 2] = new_state2[2, 2]
            new_state2[2, 2] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3),
                 new_state2.reshape(1, 3, 3)], axis=0)

        # for top side center
        if temp_state[0, 1] == -1:
            # to get three possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for right move
            new_state2 = temp_state.copy()  # for down move

            # perform left move
            new_state0[0, 1] = new_state0[0, 0]
            new_state0[0, 0] = -1

            # perform right move
            new_state1[0, 1] = new_state1[0, 2]
            new_state1[0, 2] = -1

            # perform down move
            new_state2[0, 1] = new_state2[1, 1]
            new_state2[1, 1] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3),
                 new_state2.reshape(1, 3, 3)], axis=0)

        # for bottom side center
        if temp_state[2, 1] == -1:
            # to get three possibilities
            new_state0 = temp_state.copy()  # for left move
            new_state1 = temp_state.copy()  # for right move
            new_state2 = temp_state.copy()  # for up move

            # perform left move
            new_state0[2, 1] = new_state0[2, 0]
            new_state0[2, 0] = -1

            # perform right move
            new_state1[2, 1] = new_state1[2, 2]
            new_state1[2, 2] = -1

            # perform up move
            new_state2[2, 1] = new_state2[1, 1]
            new_state2[1, 1] = -1

            new_possibilities = np.concatenate(
                [new_possibilities, new_state0.reshape(1, 3, 3), new_state1.reshape(1, 3, 3),
                 new_state2.reshape(1, 3, 3)], axis=0)

        return new_possibilities
