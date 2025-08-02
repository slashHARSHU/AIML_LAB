# ========================================================================
# helpers.py
#
# This module contains helper functions for the BFS algorithm
# to solve the 8-puzzle problem.
# It includes functions to get the start and end states,
# print states, move the empty tile, and calculate heuristics.
#
# Author: Harshad Gaikwad
# Affiliation: COEP Technical University, Pune
#
# NOTE: This code is distributed strictly for educational purposes.
# It is not intended for commercial use or distribution.
# ========================================================================

import sys
import numpy as np
from datetime import datetime


# get the elements for the start state from the user
# =======================================================================


def get_puzzle_start():
    print("-----------------------------------------------------------\n")
    print("Enter the elements of the start state for 8-puzzle problem...")
    print("Use the following order for entering...")
    print("For blank box use: -1")
    print(">>>>>>>>>>>>>>>>")
    print("0 = (0,0)    1 = (0,1)   2 = (0,2)")
    print("3 = (1,0)    4 = (1,1)   5 = (1,2)")
    print("6 = (2,0)    7 = (2,1)   8 = (2,2)")
    print("<<<<<<<<<<<<<<<<")
    elements = []
    for i in range(9):
        elements.append(int(input(f"Element {i} = ")))

    return np.array(elements).reshape(3, 3)


# get the elements for the end state from the user
# =======================================================================
def get_puzzle_end():
    print("-----------------------------------------------------------\n")
    print("Enter the end state elements similar to start state...")
    elements = []
    for i in range(9):
        elements.append(int(input(f"Element {i} = ")))

    return np.array(elements).reshape(3, 3)


# Get current date and time
# =======================================================================


def enter_date_and_time():
    print("-----------------------------------------------------------\n")
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # get a good format
    print("Current Date and Time:", timestamp)

# print required state
# =======================================================================


def print_state(state_name, state):
    print("\n>>>>>>>>>>>>>>>>")
    print(f"state = {state_name}")
    print(state)
    print("<<<<<<<<<<<<<<<<\n")


# is current state equal to the end state
# =======================================================================

def is_current_state_equal_to_end_state(current_state, end_state):
    return np.array_equal(current_state, end_state)


# calculate heuristic value for the currenty state comparin with the
# end state using the method - number of misplaced tiles
# =======================================================================


def heuristic(current_state, end_state):
    counter = 0
    for i in range(3):
        for j in range(3):
            if not end_state[i, j] == current_state[i, j]:
                counter += 1

    return counter


def heuristic_vector(new_states, end_state):
    temp_vector = []
    for state in new_states:
        temp_vector.append(int(heuristic(state, end_state)))

    return np.array(temp_vector)


def stop_function(heuristic_vector):
    if np.all(heuristic_vector == heuristic_vector[0]):
        print("Heuristics values for all nodes are same. Program ends here.")
        sys.exit()


def get_current_state_from_sorted_data(heuristic_values, new_states):
    sorted_indices = np.argsort(heuristic_values)
    sorted_states = new_states[sorted_indices]
    return sorted_states[0]
