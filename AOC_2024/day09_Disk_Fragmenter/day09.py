def get_file_path(file_name):
    import os
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

def read_input(file_path):
    with open(file_path, 'r') as file:
        digits = file.read().strip()
    # print(digits)

    disk, spaces, files=[], [], []
    for i in range(len(digits)):
        d = digits[i]
        if (i+1) % 2 == 0:
            id = "."
            spaces.append([id, len(disk), int(d)])
            # print(f"New space: {spaces[-1]}")
        else:
            id = str((i+1) // 2)
            files.append([id, len(disk), int(d)])
            # print(f"New file:  {files[-1]}")

        # print(f"Index: {i}, Digit: {d}, ID: {id}")
        new_list = [id] * int(d)
        disk.extend(new_list)
        
    return(disk, spaces, files)

def collapse_disk_byBlock(disk):
    left = 0
    right = len(disk) - 1

    while left < right:
        if disk[left] == ".":
            while right > left and disk[right] == ".":
                right -= 1
            if right > left:
                disk[left], disk[right] = disk[right], disk[left]
        left += 1

    return(disk)

def collapse_disk_byFile(disk, spaces, files):
    for file in reversed(files):
        file_id, file_start, file_length = file
        for space in spaces:
            space_id, space_start, space_length = space
            if space_length >= file_length:
                # Move file to the space
                for i in range(file_length):
                    disk[space_start + i] = file_id
                    disk[file_start + i] = space_id
                # Update space
                space[1] += file_length
                space[2] -= file_length
                break
        # print("Moved file:", file_id, "".join(disk))  # Print the disk for every file analyzed
    return disk

def compute_sum(disk):
    return sum(int(value) * index for index, value in enumerate(disk) if value != ".")

def main():
    disk1, spaces, files = read_input(get_file_path("sample.txt")) # 'sample.txt' 'input.txt'
    disk2 = disk1.copy()
    # Part 1
    # print("".join(disk1))
    disk1 = collapse_disk_byBlock(disk1)
    # print("".join(disk1))
    print(f"Day 09 - Part 1: {compute_sum(disk1)}")

    # Part 2 (solution fail for the real input even if it solve the sample...)
    # print("".join(disk2))
    disk2 = collapse_disk_byFile(disk2, spaces, files)
    print("".join(disk2))
    print(f"Day 09 - Part 2: {compute_sum(disk2)}")




if __name__ == "__main__":
    main()