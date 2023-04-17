from queue import Queue


def BFS(initial_state, goal_state):
    # initialize queue for bfs traversal
    queue = Queue()
    
    # add initial state, path to reach it, and cost to queue
    queue.put((initial_state, [], 0))
    
    # intialize set of discovered states as empty
    visited = set()

    # while the queue is not empty (we still got states to look at)
    while not queue.empty():
        # extract and dequeue "oldest" state (fifo)
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
                    if i > 0:  # tile can move up
                        # set child state as current state
                        child_state = tuple([tuple(row) for row in state])
                        # convert child state from tuple to list to make modifications
                        child_state = list(map(list, child_state))
                        # swap empty tile with tile above it
                        child_state[i][j], child_state[i-1][j] = child_state[i-1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["U"], child_cost))
                    if i < 2:  # tile can move down
                        # set child state as current state
                        child_state = tuple([tuple(row) for row in state])
                        # convert child state from tuple to list to make modifications
                        child_state = list(map(list, child_state))
                        # swap empty tile with tile below it
                        child_state[i][j], child_state[i+1][j] = child_state[i+1][j], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["D"], child_cost))
                    if j > 0:  # tile can move left
                        # set child state as current state
                        child_state = tuple([tuple(row) for row in state])
                        # convert child state from tuple to list to make modifications
                        child_state = list(map(list, child_state))
                        # swap empty tile with tile to the left of it
                        child_state[i][j], child_state[i][j-1] = child_state[i][j-1], child_state[i][j]
                        # increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
                        if tuple(map(tuple, child_state)) not in visited:
                            queue.put((child_state, path + ["L"], child_cost))
                    if j < 2:  # tile can move right
                        # set child state as current state
                        child_state = tuple([tuple(row) for row in state])
                        # convert child state from tuple to list to make modifications
                        child_state = list(map(list, child_state))
                        # swap empty tile with tile to the right of it
                        child_state[i][j], child_state[i][j+1] = child_state[i][j+1], child_state[i][j]
                        #increment the cost
                        child_cost = cost + 1
                        # if the new state hasn't been visited, enqueue it
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
        if state == goal_state:5
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
