
lines = open('./inputs/Day1.txt','r').readlines()

def replace_text_with_digits(line):
    letters = {'one': '1', 'two': '2', 'three': '3', 'four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
    return ''.join([line.replace(letter, letter[0] + letters[letter] + letter[-1]) if letter in line else line for letter in letters])

def part1(lines):
    sum = 0
    for line in lines:
        numbers = [letter for letter in line if letter.isdigit()]
        sum += int(numbers[0]+numbers[-1])
    return sum

def part2(lines):
    sum = 0
    for line in lines:
        line = replace_text_with_digits(line)
        numbers = [character for character in line if character.isdigit()]
        sum += int(numbers[0]+numbers[-1])
    return sum
print(part1(lines))
print(part2(lines))
