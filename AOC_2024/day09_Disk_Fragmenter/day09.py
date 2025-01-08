def get_file_path(file_name):
    import os
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

def read_input(file_path):
    with open(file_path, 'r') as file:
        digits = file.read().strip()
    # print(digits)

    files=[]
    for i in range(len(digits)):
        d = digits[i]
        id = "." if (i+1) % 2 == 0 else str((i+1) // 2)
        # print(f"Index: {i}, Digit: {d}, ID: {id}")
        new_list = [id] * int(d)
        files.extend(new_list)
        
    return(files)

def collapse_files(files):
    left = 0
    right = len(files) - 1

    while left < right:
        if files[left] == ".":
            while right > left and files[right] == ".":
                right -= 1
            if right > left:
                files[left], files[right] = files[right], files[left]
        left += 1

    return(files)

def main():
    files = read_input(get_file_path("input.txt")) # 'sample.txt' 'input.txt'
    # print("".join(files))
    files = collapse_files(files)
    # print("".join(files))
    total_sum = sum(int(value) * index for index, value in enumerate(files) if value != ".")
    print(f"Day 09 - Part 1: {total_sum}")


if __name__ == "__main__":
    main()