import algorithms


# function for determining solvability based on number of inversions
def solvable(initial_state):
    """ code for finding inversions in a matrix -> iterates around the edge """
    inversions = 0
    # position of numbers on edge of matrix (excludes 0 -> not needed for inversions)
    path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]

    # iterate through puzzle and get number of inversions
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
    # fastest running time
    #   initial_state = [[1, 3, 4], [8, 0, 2], [7, 6, 5]]
    # slowest running time (for DFS)
    #   initial_state = [[1, 3, 4], [8, 0, 6], [7, 5, 2]]
    
    # open file with initial state for reading
    file = open('initial_state.txt', 'r')
    # create initial_state as list of lists of tiles
    initial_state = []
    row = []
    for line in file:
        for entry in line.split():
            row.append(int(entry))
        initial_state.append(row)
        row = []

    # if the initial state is not solvable, exit the puzzle
    isSolvable = solvable(initial_state)
    if not isSolvable:
        print("Not Solvable")
        return
    
    # initialize the goal state
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    # call BFS on initial state
    state, path, cost = algorithms.BFS(initial_state, goal_state)
    print("BFS")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)

    print("\n")

    # call DFS on initial state
    state, path, cost = algorithms.DFS(initial_state, goal_state)
    print("DFS")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)

    print("\n")

    # call dijkstra on initial state
    state, path, cost = algorithms.dijkstra(initial_state, goal_state)
    print("Dijkstra")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)


main()
