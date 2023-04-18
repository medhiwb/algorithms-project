from queue import Queue
import heapq


def BFS(initial_state, goal_state):
    # initialize queue for bfs traversal
    queue = Queue()
    # add initial state, path to reach it, and cost to queue
    queue.put((initial_state, [], 0))
    # intialize set of discovered states as empty
    visited = set()

    # while the queue is not empty (we still got states to look at)
    while not queue.empty():
        # extract and dequeue "oldest" state (fifo) --> current state
        state, path, cost = queue.get()

        # if the state is the goal state, yay! end this ish
        if state == goal_state:
            return state, path, cost

        # mark state as discovered
        visited.add(tuple(map(tuple, state)))

        """ check the position of the empty tile in the matrix
            and generate child states (next possible states) by moving the empty tile """
        # for each row i and column j in the puzzle matrix...
        for i in range(0, 3):
            for j in range(0, 3):
                # once row i and column j is the location of the empty tile, enqueue all next possible states
                if state[i][j] == 0:
                    if j > 0:  # tile can move left
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile to the left of it
                        child_state[i][j], child_state[i][j - 1] = child_state[i][j - 1], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["L"], child_cost))
                    if i > 0:  # tile can move up
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile above it
                        child_state[i][j], child_state[i - 1][j] = child_state[i - 1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["U"], child_cost))
                    if j < 2:  # tile can move right
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile to the right of it
                        child_state[i][j], child_state[i][j + 1] = child_state[i][j + 1], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["R"], child_cost))
                    if i < 2:  # tile can move down
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile below it
                        child_state[i][j], child_state[i + 1][j] = child_state[i + 1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["D"], child_cost))

    return


def DFS(initial_state, goal_state):
    # initialize stack for dfs traversal
    stack = [(initial_state, [], 0)]
    # initialize set of discovered states and add initial state
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    # while the stack is not empty (still got states to look at)
    while stack:
        # extract and pop "newest" state (lifo) --> current state
        state, path, cost = stack.pop()

        # if the state is the goal state, yay! end this ish
        if state == goal_state:
            return state, path, cost

        """ check the position of the empty tile in the matrix
            and generate child states (next possible states) by moving the empty tile """
        # for each row i and column j in the puzzle matrix...
        for i in range(0, 3):
            for j in range(0, 3):
                # once row i and column j is the location of the empty tile, append all next possible states
                if state[i][j] == 0:
                    if i < 2:  # tile can move down
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile below it
                        child_state[i][j], child_state[i + 1][j] = child_state[i + 1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, append it and mark it discovered
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["D"], child_cost))
                            visited.add(tuple(map(tuple, child_state)))
                            # if the new state is goal state, end search early
                            if child_state == goal_state:
                                return child_state, path + ["D"], child_cost
                    if j < 2:  # tile can move right
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile to the right of it
                        child_state[i][j], child_state[i][j + 1] = child_state[i][j + 1], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, append it and mark it discovered
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["R"], child_cost))
                            visited.add(tuple(map(tuple, child_state)))
                            # if the new state is goal state, end search early
                            if child_state == goal_state:
                                return child_state, path + ["R"], child_cost
                    if i > 0:  # tile can move up
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile above it
                        child_state[i][j], child_state[i - 1][j] = child_state[i - 1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, append it and mark it discovered
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["U"], child_cost))
                            visited.add(tuple(map(tuple, child_state)))
                            # if the new state is goal state, end search early
                            if child_state == goal_state:
                                return child_state, path + ["U"], child_cost
                    if j > 0:  # tile can move left
                        # set child state as current state
                        child_state = list(map(list, state))
                        # swap empty tile with tile to the left of it
                        child_state[i][j], child_state[i][j - 1] = child_state[i][j - 1], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, append it and mark it discovered
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["L"], child_cost))
                            visited.add(tuple(map(tuple, child_state)))
                            # if the new state is goal state, end search early
                            if child_state == goal_state:
                                return child_state, path + ["L"], child_cost

    return


def dijkstra(initial_state, goal_state):
    queue = [(0, initial_state, [])]
    visited = set()

    while queue:
        cost, state, path = heapq.heappop(queue)
        if state == goal_state:
            return state, path, cost
        visited.add(tuple(map(tuple, state)))

        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    if j > 0:  # tile can move left
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        tile_value = child_state[i][j - 1]
                        child_state[i][j], child_state[i][j - 1] = child_state[i][j - 1], child_state[i][j]
                        child_cost = cost + tile_value
                        if tuple(map(tuple, child_state)) not in visited:
                            heapq.heappush(queue, (child_cost, child_state, path + ["L"]))
                            visited.add(tuple(map(tuple, child_state)))
                    if i > 0:  # tile can move up
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        tile_value = child_state[i-1][j]
                        child_state[i][j], child_state[i - 1][j] = child_state[i - 1][j], child_state[i][j]
                        child_cost = cost + tile_value
                        if tuple(map(tuple, child_state)) not in visited:
                            heapq.heappush(queue, (child_cost, child_state, path + ["U"]))
                            visited.add(tuple(map(tuple, child_state)))
                    if j < 2:  # tile can move right
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        tile_value = child_state[i][j+1]
                        child_state[i][j], child_state[i][j + 1] = child_state[i][j + 1], child_state[i][j]
                        child_cost = cost + tile_value
                        if tuple(map(tuple, child_state)) not in visited:
                            heapq.heappush(queue, (child_cost, child_state, path + ["R"]))
                            visited.add(tuple(map(tuple, child_state)))
                    if i < 2:  # tile can move down
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        tile_value = child_state[i+1][j]
                        child_state[i][j], child_state[i + 1][j] = child_state[i + 1][j], child_state[i][j]
                        child_cost = cost + tile_value
                        if tuple(map(tuple, child_state)) not in visited:
                            heapq.heappush(queue, (child_cost, child_state, path + ["D"]))
                            visited.add(tuple(map(tuple, child_state)))

    return
