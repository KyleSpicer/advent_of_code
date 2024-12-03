# AoC 2024, day 3

SAMPLE_1_FILE = "sample.txt"
SAMPLE_2_FILE = "sample2.txt"
DATA_FILE = "data.txt"


def is_valid_instruction(instruction):
    # count occurences of mul(
    start = "mul("
    count = instruction.count(start)

    if count > 1:
        index = instruction.rfind("mul(")
        instruction = instruction[index:]

    # validate contents of instruction
    if "," not in instruction:
        return None, False

    invalid_chars = "!@#$%^&*`/?';. "
    if any(char in invalid_chars for char in instruction):
        return None, False

    try:
        temp = instruction.replace("mul(", "")
        temp = list(map(int, temp.replace(")", "").split(",")))

    except Exception as e:
        return None, False

    if len(temp) != 2:
        return None, False

    return temp, True


def parse_valid_mul_instructions(data) -> list:
    valid_instructions = []
    temp_instructions = []
    start = "mul("
    end = ")"
    last_index = 0

    # loop to initially pull out "mul(" to ")
    while last_index < len(data):
        index = data.find(start, last_index)
        if index == -1:
            break

        end_index = data.find(end, index)
        if end_index == -1:
            break

        curr_instruction = data[index : end_index + len(end)]
        temp_instructions.append(curr_instruction)

        last_index = end_index + len(end)

    # clean temp instructions to valid_instructions
    for instruction in temp_instructions:
        confirmed_ins, is_valid = is_valid_instruction(instruction)
        if is_valid:
            valid_instructions.append(confirmed_ins)

    return valid_instructions


def calc_instructions(instruction_list) -> int:
    result = 0

    for instruction in instruction_list:
        result += instruction[0] * instruction[1]

    return result


def retrieve_do_instructions(data) -> list:
    instructions = []
    temp_instructions = []
    idx = 0

    # mul instructions enabled
    first_dont_idx = data.find("don't()", 0)
    instructions = parse_valid_mul_instructions(data[:first_dont_idx])
    data = data[first_dont_idx:]

    while idx < len(data):
        do_idx = data.find("do()", idx)
        if do_idx == -1:
            break

        do_start = do_idx + len("do()")
        dont_idx = data.find("don't()", do_start)

        if dont_idx == -1:
            scope = data[do_start:]
            idx = len(data)

        else:
            # go up to next don't()
            scope = data[do_start:dont_idx]
            idx = dont_idx + len("don't()")

        valid_instructions = parse_valid_mul_instructions(scope)
        instructions.extend(valid_instructions)

    return instructions


def part_one(data):
    result = 0

    valid_instructions = parse_valid_mul_instructions(data)

    result = calc_instructions(valid_instructions)

    return result


def part_two(data):
    result = 0
    do_instructions = retrieve_do_instructions(data)

    return calc_instructions(do_instructions)


def main():
    with open(DATA_FILE, "r") as file:
        data = file.read()

    part_one_answer = part_one(data)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(data)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
