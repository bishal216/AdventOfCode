lines = open("./../inputs/day19.txt", "r").readlines()

patterns = lines[0].strip().split(", ")
towels = [line.strip() for line in lines[2:]]

def count_ways_to_form_string(string, substrings):
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for substring in substrings:
            if i >= len(substring) and string[i - len(substring): i] == substring:
                dp[i] += dp[i - len(substring)]
    return dp[n]

print(sum(count_ways_to_form_string(towel, patterns) > 0 for towel in towels))
print(sum(count_ways_to_form_string(towel, patterns) for towel in towels))