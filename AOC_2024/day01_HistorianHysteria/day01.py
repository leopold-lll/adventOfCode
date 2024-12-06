

if __name__ == "__main__":
    # read input
    f = "input.txt"  # "sample.txt" "input.txt"
    dist = 0
    lsx, ldx = [], []
    with open(f) as fin:
        for l in fin:
            sx, dx = list(map(int, l.split()))
            lsx.append(sx)
            ldx.append(dx)
        lsx.sort()
        ldx.sort()

    # Part1
    for s, d in zip(lsx, ldx):
        # print(s, d, abs(s-d))
        dist += abs(s-d)
    print("The final distance is:  ", dist)

    # Part2
    # Dict of occurrency for right list
    occ = {}
    for d in ldx:
        if d in occ:
            occ[d] += 1
        else:
            occ[d] = 1

    # compute similarity
    sim = 0
    for s in lsx:
        if s in occ:
            # print(s, " -> ", occ[s])
            sim += (s*occ[s])
    print("The similarity score is:", sim)
