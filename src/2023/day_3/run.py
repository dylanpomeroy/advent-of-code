def identify_number(line_index, start_col_index, input,
                    already_counted_indices):
    num_string = ''
    curr_num_index = start_col_index
    input_line = input[line_index]
    while curr_num_index >= 0 and input_line[curr_num_index]\
            .isnumeric():
        num_string = input_line[curr_num_index] + num_string
        already_counted_indices.add(
            str(line_index) + '-' + str(curr_num_index))
        curr_num_index -= 1
    curr_num_index = start_col_index + 1
    while curr_num_index < len(input[0]) \
            and input_line[curr_num_index].isnumeric():
        num_string = num_string + \
            input_line[curr_num_index]
        already_counted_indices.add(
            str(line_index) + '-' + str(curr_num_index))
        curr_num_index += 1

    return int(num_string)


def get_numbers_surrounding(line_index, col_index, input,
                            already_counted_indices):
    numbers = []
    for line_search_index in range(line_index - 1, line_index + 2):
        if line_search_index > len(input):
            continue
        for col_search_index in range(col_index - 1, col_index + 2):
            if col_search_index > len(input[0]):
                continue

            is_number = input[line_search_index][col_search_index].isnumeric()
            is_new = not str(line_search_index) + '-' + \
                str(col_search_index) in already_counted_indices
            if not is_number or not is_new:
                continue
            number = identify_number(
                line_search_index, col_search_index, input,
                already_counted_indices)
            numbers.append(number)

    return numbers


def part_1(input):
    result = 0
    already_counted_indices = set()
    for line_index, line in enumerate(input):
        for col_index in range(0, len(line)):
            curr_char = input[line_index][col_index]
            if curr_char.isnumeric() or curr_char == '.':
                continue
            surrounding_numbers = get_numbers_surrounding(
                line_index, col_index, input, already_counted_indices)
            result += sum(surrounding_numbers)

    return result


def part_2(input):
    result = 0
    already_counted_indices = set()
    for line_index, line in enumerate(input):
        for col_index in range(0, len(line)):
            curr_char = input[line_index][col_index]
            if curr_char != '*':
                continue
            numbers_surrounding = get_numbers_surrounding(
                line_index, col_index, input, already_counted_indices)
            if len(numbers_surrounding) != 2:
                continue
            result += numbers_surrounding[0] * numbers_surrounding[1]

    return result
