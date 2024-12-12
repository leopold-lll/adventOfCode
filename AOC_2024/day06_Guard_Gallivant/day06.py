import re
from pprint import pprint


def read_input(file_name="sample.txt"):
    with open(file_name) as fin:
        map = [list(line.strip()) for line in fin]
        guard = next((i, j) for i, row in enumerate(map)
                     for j, char in enumerate(row) if char == '^')
    return (map, guard)


def step(tuple1, tuple2, D):
    t = tuple(a + b for a, b in zip(tuple1, tuple2))
    if t[0] < 0 or t[0] >= D or t[1] < 0 or t[1] >= D:
        return (t, True)
    return (t, False)


def navigate(map, guard):
    d = 0  # direction 0=up, 1=right, 2=down, 3=left
    dir = {0: (-1, 0), 1: (0, +1), 2: (+1, 0), 3: (0, -1)}
    D = len(map)
    g_now = guard
    steps = 1

    # print(guard)
    # pprint(map)
    # print("")
    map[g_now[0]][g_now[1]] = "X"  # only for first position
    while True:
        # Check next position
        g_next, exit = step(g_now, dir[d], D)
        if not exit and map[g_next[0]][g_next[1]] == "#":
            d = (d+1) % 4  # Rotate
            g_next, exit = step(g_now, dir[d], D)

        if exit:
            print("Part1: The guard has exit after ", steps, "steps")  # 5318
            # pprint(map)
            break

        # Move
        g_now = g_next
        if map[g_now[0]][g_now[1]] == ".":
            map[g_now[0]][g_now[1]] = "X"
            steps += 1

    # pprint(map)


if __name__ == "__main__":
    map, guard = read_input("input.txt")
    navigate(map, guard)
