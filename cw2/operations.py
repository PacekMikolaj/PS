def first_character(string):
    return string[0]


def first_two_characters(string):
    if len(string) < 2:
        return ''
    return string[:2]


def all_characters_except_first_two(string):
    return string[2:]


def penultimate_character(string):
    if len(string) < 2:
        return ''
    return string[-2]


def last_three_characters(string):
    if len(string) < 2:
        return ''
    return string[-3:]


def all_characters_in_even_positions(string):
    return string[::2]
