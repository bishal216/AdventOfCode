lines = [line.strip().split()  for line in open('./inputs/day7.txt', 'r').readlines()]

def get_precedence_part1(card_hand):
    card_counts = sorted([card_hand.count(card) for card in set(card_hand)])
    if max(card_counts) > 3:
        return max(card_counts) + 1
    if max(card_counts) == 3:
        return 4 if 2 in card_counts else 3
    return card_counts.count(2)

def part1(lines):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    new_lines = sorted(lines, key=lambda x: [cards.index(val) for val in x[0]], reverse=True)
    card_ranks = sorted([(line[0], int(line[1]), get_precedence_part1(line[0])) for line in new_lines], key = lambda x:x[2])
    return sum([card[1] * (card_ranks.index(card) + 1) for card in card_ranks])

def get_precedence_part2(card_hand):
    card_counts = sorted([card_hand.count(card) for card in set(card_hand) if card != 'J'])
    if not card_counts:
        return 6
    card_counts = card_counts[:-1] + [card_counts[-1] + card_hand.count('J')]
    if max(card_counts) > 3:
        return max(card_counts) + 1
    if max(card_counts) == 3:
        return 4 if 2 in card_counts else 3
    return card_counts.count(2)

def part2(lines):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    new_lines = sorted(lines, key=lambda x: [cards.index(val) for val in x[0]], reverse=True)
    card_ranks = sorted([(line[0], int(line[1]), get_precedence_part2(line[0])) for line in new_lines], key = lambda x:x[2])
    return sum([card[1] * (card_ranks.index(card) + 1) for card in card_ranks])

print(part1(lines))
print(part2(lines))