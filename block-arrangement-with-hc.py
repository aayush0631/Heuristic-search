def heuristic_distance(blocks, goal):
    """Heuristic: sum of index differences from goal positions."""
    return sum(abs(i - goal.index(block)) for i, block in enumerate(blocks))

def generate_adjacent_swaps(blocks):
    """Generate neighbors by swapping adjacent elements."""
    neighbors = []
    for i in range(len(blocks) - 1):
        neighbor = blocks.copy()
        neighbor[i], neighbor[i + 1] = neighbor[i + 1], neighbor[i]
        neighbors.append((neighbor, f"swap({i}, {i + 1})"))
    return neighbors

def hill_climb_sort(start, goal):
    """Hill climbing to sort blocks into goal order using adjacent swaps."""
    blocks = start
    score = heuristic_distance(blocks, goal)
    steps = []

    print("Start State:", blocks)
    print("Initial Heuristic:", score)
    print()

    while True:
        neighbors = generate_adjacent_swaps(blocks)
        best_neighbor = None
        best_score = score

        for new_state, action in neighbors:
            h = heuristic_distance(new_state, goal)
            print(f"Checking {new_state} → Heuristic: {h}")
            if h < best_score:
                best_score = h
                best_neighbor = (new_state, action)

        print()

        if best_neighbor is None:
            print("No better move. Local minimum reached.")
            break

        blocks, action = best_neighbor
        steps.append(action)
        score = best_score

        print(f"Perform: {action}")
        print("New State:", blocks)
        print("New Heuristic:", score)
        print()

        if score == 0:
            print("Goal Reached!")
            break

    print("\nFinal Result:")
    print("State:", blocks)
    print("Moves:", steps)
    print("Success!" if blocks == goal else "Stuck before reaching goal.")

# Example usage
initial = ['C', 'A', 'D', 'B']
goal = ['A', 'B', 'C', 'D']

hill_climb_sort(initial, goal)
