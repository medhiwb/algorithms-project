import algorithms


# function for determining solvability based on number of inversions
def solvable(initial_state):
    """ code for finding inversions in a matrix -> iterates around the edge """
    inversions = 0
    # position of numbers on edge of matrix (excludes 0 -> not needed for inversions)
    path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        for j in range(i + 1, len(path)):
            x2, y2 = path[j]
            if initial_state[x1][y1] > initial_state[x2][y2]:
                inversions += 1

    # even inversions = solvable
    if inversions % 2 == 0:
        return True
    else:
        return False


def main():
    
    # initial_state = [[5, 6, 7], [4, 0, 8], [3, 2, 1]]
    # initial_state = [[1, 3, 4], [8, 0, 2], [7, 6, 5]]
    initial_state = [[1, 3, 4], [8, 0, 6], [7, 5, 2]]
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    isSolvable = solvable(initial_state)
    if not isSolvable:
        print("Not Solvable")
        return

    state, path, cost = algorithms.BFS(initial_state, goal_state)
    print("State:", state)
    print("BFS Path:", path)
    print("BFS Cost:", cost)

    print("\n")

    state, path, cost = algorithms.DFS(initial_state, goal_state)
    print("State:", state)
    print("DFS Path:", path)
    print("DFS Cost:", cost)

    print("\n")

    state, path, cost = algorithms.dijkstra(initial_state, goal_state)
    print("State:", state)
    print("Dijkstra Path:", path)
    print("Dijkstra Cost:", cost)


main()
