# AoC 2024, day 9

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"
SAMPLE_2_FILE = "12345.txt"

from copy import copy

is_part_two = False


def shift_disk(file_sys):
    back_ptr = len(file_sys) - 1

    for i, num in enumerate(file_sys):
        if "." == num:
            while back_ptr > i:
                if file_sys[back_ptr] != ".":
                    file_sys[back_ptr], file_sys[i] = file_sys[i], file_sys[back_ptr]
                    back_ptr -= 1
                    break
                else:
                    back_ptr -= 1
    return file_sys


def calc_checksum(file_sys) -> int:
    total = 0
    for i, num in enumerate(file_sys):
        try:
            total += i * int(num)
        except ValueError:
            continue
    return total


def part_one(disk_map):
    file_sys = list(map(int, disk_map))
    idx = 0
    new_file_sys = []

    for i, file in enumerate(file_sys):
        if i % 2 != 0:
            continue  # skip sizes
        else:
            id_num = idx
            if (i + 1) < len(file_sys):
                size = file_sys[i + 1]
            else:
                size = 0
            idx += 1
            curr = [id_num] * file
            curr.extend(["."] * size)
            new_file_sys.extend(curr)

    updated_file_sys = shift_disk(new_file_sys)

    return calc_checksum(updated_file_sys)


def part_two(disk_map):
    disk_map = list(map(int, disk_map))

    files = {}  # file_id : (index, size)
    spaces = []
    is_file = True
    ptr = 0

    # stores starting index and size of current chunk
    for i, size in enumerate(disk_map):
        if is_file:
            files[i // 2] = (ptr, size)
        else:
            spaces.append((ptr, size))
        is_file = not is_file  # alternate between files and spaces
        ptr += size

    # iter over files in reverse order
    for file_id in reversed(files):
        loc, file_size = files[file_id]
        space_id = 0

        # loop over spaces
        while space_id < len(spaces):
            space_loc, space_size = spaces[space_id]
            if space_loc > loc:
                # skip spaces after current file location
                break

            if space_size == file_size:
                # updates files dict, remove spaces from list
                files[file_id] = (space_loc, file_size)
                spaces.pop(space_id)
                break

            if space_size > file_size:
                # relocate file to start of space, update spaces new remaining size
                files[file_id] = (space_loc, file_size)
                spaces[space_id] = (space_loc + file_size, space_size - file_size)
                break

            # checked entire space and it is too large, continue
            space_id += 1

    # calc checksum
    checksum = 0
    for file_id, (loc, size) in files.items():
        for i in range(loc, loc + size):
            checksum += file_id * i

    return checksum


def main():
    with open(DATA_FILE, "r") as file:
        disk_map = file.read().strip()

    part_one_answer = part_one(copy(disk_map))
    print(f"{part_one_answer = }")

    part_two_answer = part_two(copy(disk_map))
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
