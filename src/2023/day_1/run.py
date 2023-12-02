
def part_1(input):
    return 0


def part_2(input):
    number_words = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]

    nums_to_add = []
    for line in input:
        numbers = []
        for index, char in enumerate(line):
            if char.isnumeric():
                numbers.append(int(char))
                continue
            for number_word_index, number_word in enumerate(number_words):
                if line[index:len(number_word) + index] == number_word:
                    numbers.append(number_word_index)
                    continue

        nums_to_add.append(numbers[0] * 10 + numbers[-1])

    return sum(nums_to_add)
