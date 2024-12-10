lines = open("./../inputs/day7.txt", "r").readlines()
lines = [line.strip() for line in lines]

def plus_one_base_n(number_string, base):
    decimal_value = int(number_string, base)
    incremented_value = decimal_value + 1
    result = ""
    while incremented_value > 0:
        result = str(incremented_value % base) + result
        incremented_value //= base
    return result.zfill(len(number_string))

def check_calc(target_total, numbers, base):
    target_total = int(target_total)
    operator_combination = "0" * (len(numbers) - 1)
    while True:
        current_result = int(numbers[0])
        for i, num in enumerate(numbers[1:]):
            if operator_combination[i] == "0":
                current_result += int(num)
            elif operator_combination[i] == "1":
                current_result *= int(num)
            elif operator_combination[i] == "2":
                current_result = int(str(current_result) + str(num))
        if current_result == target_total:
            return True
        operator_combination = plus_one_base_n(operator_combination, base)
        operator_combination = operator_combination.zfill(len(numbers) - 1)
        if len(operator_combination) > len(numbers) - 1:
            break
    return False

def part1(lines):
    total_sum = 0
    for line in lines:
        target_total, numbers = line.split(":")
        numbers = numbers.split()
        if check_calc(target_total, numbers, 2):
            total_sum += int(target_total)
    return total_sum

def part2(lines):
    total_sum = 0
    for line in lines:
        target_total, numbers = line.split(":")
        numbers = numbers.split()
        if check_calc(target_total, numbers, 3):
            total_sum += int(target_total)
    return total_sum

print(part1(lines))
print(part2(lines))
