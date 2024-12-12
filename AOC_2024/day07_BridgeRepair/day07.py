import re
from pprint import pprint

def get_file_path(file_name):
    import os
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    sums, elements = [], []
    for line in lines:
        parts = list(map(int, re.split(r'[: ]+', line.strip())))
        sums.append(parts[0])
        elements.append(parts[1:])

    return sums, elements

def check_calibration(sum_to_check, sum, elements, part2=False):
    if elements:
        return max(
            check_calibration(sum_to_check, sum+elements[0], elements[1:], part2), 
            check_calibration(sum_to_check, sum*elements[0], elements[1:], part2),
            check_calibration(sum_to_check, multiply_and_add(sum, elements[0]), elements[1:], part2) if part2 else 0
        )
    else:
        if sum == sum_to_check:
            print("  Found correct sum (" + ("Part2" if part2 else "Part1") + "):", sum_to_check)
            return sum
        else:
            return 0

def multiply_and_add(a, b):
    power_of_10 = 10 ** (len(str(b)))
    return a * power_of_10 + b
        

if __name__ == "__main__":
    sums, elements = read_input(get_file_path("sample.txt"))
    part1, part2 = 0, 0
    for s, e in zip(sums, elements):
        print(s, e)    
        part1 += check_calibration(s, e[0], e[1:])
        part2 += check_calibration(s, e[0], e[1:], part2=True)
    
    # print("Max elements len:", max([len(e) for e in elements]))
    print("Part1 (+*),   the sum of the correct sums is:", part1) # 5837374519342
    print("Part2 (+*||), the sum of the correct sums is:", part2) # 492383931650959

    # Tests:
    # print(multiply_and_add(123, 456)) # 123456