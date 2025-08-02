import sys
import helpers as hlp

hlp.enter_date_and_time()
start_state = hlp.get_puzzle_start()
end_state = hlp.get_puzzle_end()
hlp.print_state("start state", start_state)
hlp.print_state("end state", end_state)

# if start and end states are equal then stop the code
if hlp.np.array_equal(start_state, end_state):
    print("Start and End states are similar. Program ends here.")
    sys.exit()

# get the solution queue and removed element queue
queue = hlp.np.empty((0, 3, 3), dtype=int)
removed_state_queue = hlp.np.empty((0, 3, 3), dtype=int)

# add start state to queue
queue = hlp.np.concatenate([queue, start_state.reshape(1, 3, 3)], axis=0)

# start the while loop and make the start state as current state
current_state = start_state.copy()

while not hlp.heuristic(current_state, end_state) == 0:
    new_states = hlp.move_empty_tile(current_state)
    heuristic_values = hlp.heuristic_vector(new_states, end_state)
    hlp.stop_function(heuristic_values)
    current_state = hlp.get_current_state_from_sorted_data(
        heuristic_values, new_states)
    print(current_state)
