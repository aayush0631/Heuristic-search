from heapq import heappush, heappop
import copy

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def manhattan_distance(state):
    """Manhattan distance for debugging or evaluation (not used in UCS)."""
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                dist += abs(goal_i - i) + abs(goal_j - j)
    return dist

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(num for row in state for num in row)

def is_goal(state):
    return state == GOAL_STATE

def generate_neighbors(state):
    i, j = get_blank_position(state)
    neighbors = []
    for move, (di, dj) in MOVES.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append((move, new_state))
    return neighbors

def uniform_cost_search(start):
    visited = set()
    heap = []
    heappush(heap, (0, start, []))

    print("Initial State:")
    for row in start:
        print(row)
    print("Initial Manhattan Distance:", manhattan_distance(start))
    print()

    while heap:
        cost, current_state, path = heappop(heap)
        key = state_to_tuple(current_state)

        if key in visited:
            continue
        visited.add(key)

        print(f"Exploring (Cost: {cost}):")
        for row in current_state:
            print(row)
        print("Manhattan Distance:", manhattan_distance(current_state))
        print()

        if is_goal(current_state):
            print("Goal reached!")
            return path

        for move, neighbor in generate_neighbors(current_state):
            neighbor_key = state_to_tuple(neighbor)
            if neighbor_key not in visited:
                heappush(heap, (cost + 1, neighbor, path + [move]))

    return None

# Example run
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]

solution = uniform_cost_search(initial_state)

if solution:
    print("Solution path:")
    print(solution)
else:
    print("No solution found.")
