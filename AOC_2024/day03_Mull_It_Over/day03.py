import re


def find_mul(text):
    pattern_mul = r'mul\((\d{1,3}),(\d{1,3})\)'
    v_mul = re.findall(pattern_mul, text)
    # print(v_mul)
    sum = 0
    for x, y in v_mul:
        sum += (int(x)*int(y))
    # print("Partial sum is: ", sum)
    return (sum)


def part2(text):
    # Ripulisco con le sole info importanti (senza c'era qualche bug...)
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)
    clean_text = " ".join(matches)

    pattern_do = r"(do|don't)\(\)(.*?)(?=(do|don't)\(\)|$)"
    v_do = re.findall(pattern_do, clean_text)
    # [print(d) for d in v_do if d[0] == "do"]
    sum = 0
    for x in v_do:
        if x[0] == "do":
            sum += find_mul(x[1])
    return sum


if __name__ == "__main__":
    # read input
    f = "input.txt"  # "sample.txt" "input.txt"
    with open(f) as fin:
        text = "do()"+fin.read()

    sum1 = find_mul(text)  # Part1
    sum2 = part2(text)    # Part2

    print("The sum of the multiplications is: \npart1: ", sum1, "\npart2: ", sum2)
