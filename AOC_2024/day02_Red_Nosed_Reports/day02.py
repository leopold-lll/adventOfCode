
def check_report(r):
    # print("")
    # print(r)
    if len(r) == 1:
        return 1
    else:
        if r[1] == r[0]:
            return 0
        else:
            order = 1 if r[1] > r[0] else -1  # crescente
            # print("order", order)

            diffs = []
            for i in range(len(r)-1):
                diff = (r[i+1] - r[i])*order
                diffs.append(diff)
            # print(diffs)
            ma = max(diffs)
            mi = min(diffs)
            # print(mi, ma)
            if mi > 0 and ma <= 3:
                # print("SAFE")
                return 1
            else:
                # print("NOT SAFE")
                return 0


if __name__ == "__main__":
    # read input
    reports = []
    f = "input.txt"  # "sample.txt" "input.txt"
    with open(f) as fin:
        for l in fin:
            x = [int(n) for n in l.strip("\n").split(" ")]
            reports.append(x)

    nSafe = 0
    for r in reports:
        # PART1: nSafe += check_report(r)
        # PART2:
        # Terribile soluzione con complessità n^2 ma è stata la più veloce da implementare...
        # print("\n\nNEW REPORT")
        for i in range(-1, len(r)):
            # print("i:", i)
            tmp_r = [r[j] for j in range(len(r)) if j != i]
            tmp_check = check_report(tmp_r)
            if tmp_check == 1:
                nSafe += 1
                break
    print("nSafe:", nSafe)
