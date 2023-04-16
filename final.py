def solvable(initial_state):
    inversions = 0
    for j in range(len(initial_state)):
        for k in range(j + 1, 9):
            if initial_state[j] and initial_state[k] and initial_state[j] > initial_state[k]:
                inversions += 1
    print(inversions)

    if inversions % 2 == 0:
        return True
    else:
        return False


def main():
    initial_state = [7, 2, 4, 6, 1, 3, 8, 5, 0]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    isSolvable = solvable(initial_state)
    if not isSolvable:
        print("Not Solvable")
        return


main()
