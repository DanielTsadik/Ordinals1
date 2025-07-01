from collections import defaultdict

# Transition table for the Turing Machine in Exercise 1
# Format: (current_state, current_symbol) => (write_symbol, move_direction, next_state)
transitions = {
    ('A', 0): (1, 'R', 'B'),
    ('A', 1): (1, 'L', 'C'),
    ('B', 0): (1, 'R', 'C'),
    ('B', 1): (1, 'R', 'B'),
    ('C', 0): (1, 'R', 'D'),
    ('C', 1): (0, 'L', 'E'),
    ('D', 0): (1, 'L', 'A'),
    ('D', 1): (1, 'L', 'D'),
    ('E', 0): ('halt',),
    ('E', 1): (0, 'L', 'A')
}

def simulate_turing_machine(max_steps=47_176_870):
    tape = defaultdict(int)  # Infinite tape initialized with 0s
    head = 0                 # Head starts at position 0
    state = 'A'              # Initial state
    steps = 0

    while steps < max_steps:
        symbol = tape[head]
        key = (state, symbol)

        if key not in transitions:
            print(f"❌ Undefined transition at step {steps}.")
            return

        result = transitions[key]
        if result[0] == 'halt':
            print(f"✅ Machine halts after {steps + 1} steps.")
            return

        write_symbol, move, next_state = result
        tape[head] = write_symbol
        head += 1 if move == 'R' else -1
        state = next_state
        steps += 1

    print(f"⚠️ Machine did not halt within {max_steps} steps.")

# Run the simulation
simulate_turing_machine()