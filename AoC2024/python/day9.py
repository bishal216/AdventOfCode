line = open("./../inputs/day9.txt", "r").readline().strip()

def get_string(line):
    string_list = []
    count = 0
    for i in range(0, len(line)):
        if i % 2 == 0:
            string_list.extend([str(count)] * int(line[i]))
            count += 1
        else:
            string_list.extend(["."] * int(line[i]))
    reversed_parsed_string = [i for i in reversed(string_list) if i != "."]
    return string_list, reversed_parsed_string

def part1(line):
    string_list, reversed_parsed_string = get_string(line)
    c = 0
    for i, item in enumerate(string_list):
        if item == ".":
            string_list[i] = reversed_parsed_string[c]
            c += 1
    return sum(i * int(item) for i, item in enumerate(string_list[:len(reversed_parsed_string)]))

def get_pattern_range(lst, sublst, slength):
    for i in range(len(lst) - slength + 1):
        if lst[i: i + slength] == sublst:
            return i
    return None

def replace_first_pattern(lst, num, length):
    num_i = get_pattern_range(lst, [num] * length, length)
    blank_i = get_pattern_range(lst,["."] * length, length)
    if not blank_i:
        return lst
    if num_i > blank_i:
        lst[num_i:num_i + length] = ["."] * length
        lst[blank_i:blank_i + length] = [num] * length
    return lst

def part2(line):
    string_list, reversed_parsed_string = get_string(line)
    for item in sorted(set(reversed_parsed_string), reverse=True):
        string_list = replace_first_pattern(string_list, item, reversed_parsed_string.count(item))
    print("".join(string_list))
    return sum(i * int(item) for i, item in enumerate(string_list) if item != ".")

print(part1(line))
# print(part2(line))
