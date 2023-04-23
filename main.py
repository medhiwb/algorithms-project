import algorithms
import time


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
    start_time1 = time.time()  # start time
    state, path, cost = algorithms.BFS(initial_state, goal_state)
    print("BFS")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)

    end_time1 = time.time()  # end time
    elapsed_time1 = end_time1 - start_time1  # calculate elapsed time
    print(f"Elapsed time: {elapsed_time1} seconds")

    print("\n")

    # call DFS on initial state
    start_time2 = time.time()  # start time
    state, path, cost = algorithms.DFS(initial_state, goal_state)
    print("DFS")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)

    end_time2 = time.time()  # end time
    elapsed_time2 = end_time2 - start_time2  # calculate elapsed time
    print(f"Elapsed time: {elapsed_time2} seconds")

    print("\n")

    # call dijkstra on initial state
    start_time3 = time.time()  # start time
    state, path, cost = algorithms.Dijkstra(initial_state, goal_state)
    print("Dijkstra")
    print("-------")
    print("Cost:", cost)
    print("Path:", path)

    end_time3 = time.time()  # end time
    elapsed_time3 = end_time3 - start_time3  # calculate elapsed time
    print(f"Elapsed time: {elapsed_time3} seconds")


main()
