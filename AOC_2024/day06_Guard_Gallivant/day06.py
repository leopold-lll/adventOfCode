import re
from pprint import pprint

dir = {0: (-1, 0), 1: (0, +1), 2: (+1, 0), 3: (0, -1)}


def read_input(file_name="sample.txt"):
    with open(file_name) as fin:
        mapp = [list(line.strip()) for line in fin]
        guard = next((i, j) for i, row in enumerate(mapp)
                     for j, char in enumerate(row) if char == '^')
    return (mapp, guard)


def step(tuple1, tuple2, D):
    t = tuple(a + b for a, b in zip(tuple1, tuple2))
    if t[0] < 0 or t[0] >= D or t[1] < 0 or t[1] >= D:
        return (t, True)
    return (t, False)


def print_mapp(mapp):
    # Utility function for debug!
    D = len(mapp)
    print(" ".join(map(str, list(range(-1, D)))))
    r = 0
    for row in mapp:
        print(r, " ", end="")
        r += 1
        [print(" ".join([str(el) for el in row]))]


def check_line_intersection(mapp, g, d, depth):
    # print("depth:", depth)
    if depth == 7:
        return False
    # print(" "*depth, "Checking from:", g)
    exitFound = False
    move = dir[d]
    D = len(mapp)
    g_check = g
    g_before = g
    while not exitFound:
        # print(" "*depth, "  verify:", g_check, " -> ",
        #   mapp[g_check[0]][g_check[1]], (d+1) % 4)
        if mapp[g_check[0]][g_check[1]] == d:
            return True
        elif mapp[g_check[0]][g_check[1]] == ((d+1) % 4):
            g_over, _exit = step(g_check, move, D)
            return (not _exit and mapp[g_over[0]][g_over[1]] == "#")
        elif mapp[g_check[0]][g_check[1]] == "#":
            # Hit a wall and go deeper in the white rabbit hole!
            # Huge complexity hidden (hope it will work)
            return check_line_intersection(
                mapp, g_before, (d+1) % 4, depth+1)
        else:
            g_before = g_check
            g_check, exitFound = step(g_before, move, D)

    return False


def navigate(mapp, g_start):
    d = 0  # direction 0=up, 1=right, 2=down, 3=left
    D = len(mapp)
    g_now = g_start
    steps = 1
    obstacles = set()

    # print(g_start)
    # print_mapp(mapp)
    # print("")
    mapp[g_now[0]][g_now[1]] = 0  # only for first position
    while True:
        # Check next position
        g_next, exit = step(g_now, dir[d], D)
        if not exit and mapp[g_next[0]][g_next[1]] == "#":
            d = (d+1) % 4  # Rotate
            g_next, exit = step(g_now, dir[d], D)

        # Out of map!
        if exit:
            obstacles.discard(g_start)
            pprint(obstacles)
            print("Part1: The guard has exit after:", steps, "steps")  # 5318
            print("Part2: The obstacles could be:  ",
                  len(obstacles))  # 676 (too low...)
            break
        # print_mapp(mapp)

        # Try to place obstacle ()
        # if mapp[g_next[0]][g_next[1]] == ((d+1) % 4):
        d_tmp = (d+1) % 4
        if check_line_intersection(mapp, g_next, d_tmp, depth=0):

            obst, exit = step(g_next, dir[d], D)  # 2 step ahead
            # print("  Potential obstacle:", obst)
            if not exit and mapp[obst[0]][obst[1]] != "#":
                obstacles.add(obst)
                # print("    Obst added!")

        # Move
        g_now = g_next
        if mapp[g_now[0]][g_now[1]] == ".":
            mapp[g_now[0]][g_now[1]] = d
            steps += 1


if __name__ == "__main__":
    mapp, guard = read_input("sample_complex.txt")
    navigate(mapp, guard)
    print_mapp(mapp)
