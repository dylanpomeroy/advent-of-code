
def part_1(input):
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    result = 0

    for row in input:
        invalid_game = False
        game_id = int(row.split('Game ')[1].split(':')[0])
        rounds_text = row.split(': ')[1].split(';')
        for round_text in rounds_text:
            if invalid_game:
                break
            color_groups = list(
                map(lambda x: x.strip(), round_text.split(', ')))
            for color_group in color_groups:
                amount = int(color_group.split(' ')[0])
                color = color_group.split(' ')[1]
                if amount > limits[color]:
                    invalid_game = True
                    break

        if not invalid_game:
            result += game_id

    return result


def part_2(input):
    result = 0

    for row in input:
        minimums = {}

        rounds_text = row.split(': ')[1].split(';')
        for round_text in rounds_text:
            color_groups = list(
                map(lambda x: x.strip(), round_text.split(', ')))
            for color_group in color_groups:
                amount = int(color_group.split(' ')[0])
                color = color_group.split(' ')[1]
                minimums[color] = max(minimums.get(color, 0), amount)

        power = 1
        for minimum in minimums.values():
            power *= minimum
        result += power

    return result
