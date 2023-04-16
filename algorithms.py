from queue import Queue


def BFS(initial_state, goal_state):
    queue = Queue()
    # add initial state, path to reach it, and cost to queue
    queue.put((initial_state, [], 0))
    visited = set()

    while not queue.empty():
        state, path, cost = queue.get()
        if state == goal_state:
            return state, path, cost
        visited.add(tuple(map(tuple, state)))

        """ check the position of the empty tile in the matrix
            and generate child states by moving the empty tile """
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    if i > 0:  # tile can move up
                        child_state = tuple([tuple(row) for row in state])
                        # swap empty tile with tile above it
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i-1][j] = child_state[i-1][j], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["U"], child_cost))
                    if i < 2:  # tile can move down
                        child_state = tuple([tuple(row) for row in state])
                        # swap empty tile with tile below it
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i+1][j] = child_state[i+1][j], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["D"], child_cost))
                    if j > 0:  # tile can move left
                        child_state = tuple([tuple(row) for row in state])
                        # swap empty tile with tile above it
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i][j-1] = child_state[i][j-1], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["L"], child_cost))
                    if j < 2:  # tile can move right
                        child_state = tuple([tuple(row) for row in state])
                        # swap empty tile with tile above it
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i][j+1] = child_state[i][j+1], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["R"], child_cost))
    return -1

def isEmpty(self):
        return self.size() == 0

def DFS(inital_state, goal_state):
    stack = [(inital_state, [], 0)]
    visited = set()

    while stack:
        state, path, cost = stack.pop()
        if state == goal_state:
            return state, path, cost
        visited.add(tuple(map(tuple, state)))

        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    if j < 2:  # tile can move right
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i][j+1] = child_state[i][j+1], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["R"], child_cost))
                    if j > 0:  # tile can move left
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i][j-1] = child_state[i][j-1], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["L"], child_cost))
                    if i < 2:  # tile can move down
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i+1][j] = child_state[i+1][j], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["D"], child_cost))
                    if i > 0:  # tile can move up
                        child_state = tuple([tuple(row) for row in state])
                        child_state = list(map(list, child_state))
                        child_state[i][j], child_state[i-1][j] = child_state[i-1][j], child_state[i][j]
                        child_cost = cost + 1
                        if tuple(map(tuple, child_state)) not in visited:
                            stack.append((child_state, path + ["U"], child_cost))
        if not stack:
            break
    return -1