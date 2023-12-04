def parse_nums(nums_str):
    nums_str = nums_str.replace('  ', ' ').strip()
    return list(map(lambda num_str: int(num_str), nums_str.split(' ')))


def parse_game(game_str):
    card_num = int(game_str.split('Card ')[1].split(':')[0]) - 1
    win_nums = parse_nums(game_str.split(': ')[1].split(' | ')[0])
    your_nums = parse_nums(game_str.split(' | ')[1])

    return card_num, win_nums, your_nums


def part_1(input):
    result = 0
    for line in input:
        _, win_nums, your_nums = parse_game(line)
        score = 0
        for your_num in your_nums:
            if your_num in win_nums:
                score = score * 2 if score != 0 else 1
        result += score
    return result


def part_2(input):
    card_counts = []
    match_counts_memo = {}

    for line in input:
        card_num, win_nums, your_nums = parse_game(line)
        matches = sum([1 for your_num in your_nums if your_num in win_nums])
        match_counts_memo[card_num] = matches
        card_counts.append(1)

    for card_num in range(0, len(card_counts)):
        matches = match_counts_memo[card_num]
        for new_card_num in range(card_num + 1, card_num + 1 + matches):
            card_counts[new_card_num] += card_counts[card_num]

    return sum(card_counts)
