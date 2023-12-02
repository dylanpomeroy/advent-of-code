def read_input_lines(filename):
    file = open(filename)
    lines = file.readlines()

    result = list(map(lambda line: line.strip(), lines))
    return result
