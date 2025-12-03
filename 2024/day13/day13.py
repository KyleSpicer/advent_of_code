# AoC 2024, day 13

# 3 tokens to push A
# 1 token to push B

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"


def parse_button_configs(data) -> list:
    button_configs = []

    for i, config in enumerate(data):
        curr_config = {}
        curr = config.split("\n")

        curr_config["IDX"] = i
        curr_config["TOTAL_COINS"] = 0
        curr_config["POSSIBLE"] = False
        for i, instruction in enumerate(curr):
            if i == 0:  # A
                x = int((instruction.split("+")[1].split(", "))[0])
                y = int(instruction.split("+")[2])
                curr_config["A"] = [x, y]

            if i == 1:  # B
                x = int((instruction.split("+")[1].split(", "))[0])
                y = int(instruction.split("+")[2])
                curr_config["B"] = [x, y]

            if i == 2:  # PRIZE
                x = int((instruction.split("=")[1].split(", "))[0])
                y = int(instruction.split("=")[2])
                curr_config["PRIZE"] = [x, y]

        button_configs.append(curr_config)

    return button_configs


def process_config(config, is_part_one):
    total_a_coins = 0
    total_b_coins = 0

    ax, ay = config["A"]
    bx, by = config["B"]
    px, py = config["PRIZE"]

    if not is_part_one:
        px += 10000000000000
        py += 10000000000000

    a_button_presses = (px * by - py * bx) / (ax * by - ay * bx)
    b_button_presses = (px - ax * a_button_presses) / bx

    if (a_button_presses % 1 == b_button_presses % 1) and (b_button_presses % 1 == 0):
        return a_button_presses * 3 + b_button_presses

    return 0


def part_one(button_configs, is_part_one):
    total_presses = 0

    for config in button_configs:
        total_presses += process_config(config, is_part_one)

    return int(total_presses)


def main():
    with open(DATA_FILE, "r") as file:
        data = file.read().split("\n\n")

    button_configs = parse_button_configs(data)

    part_one_answer = part_one(button_configs, True)
    print(f"{part_one_answer = }")

    part_two_answer = part_one(button_configs, False)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
