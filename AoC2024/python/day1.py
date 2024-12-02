lines = open('./../inputs/day1.txt','r').readlines() # Read input linewise

lines = [line.rstrip().split() for line in lines] # Split each line into two numbers
left_list = [int(line[0]) for line in lines] # Get a list of first numbers
right_list = [int(line[-1]) for line in lines] # Get a list of second numbers

part1_sim_score = sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list))) # Absolute differences between sorted left and sorted right list
part2_sim_score = sum(i * right_list.count(i) for i in left_list) # Multiply value in left list by count in second list

print(part1_sim_score, part2_sim_score)

# def part1(left_list, right_list):
#     llist = sorted(left_list)
#     rlist = sorted(right_list)
#     sim_score = 0
#     for i in range(len(llist)):
#         sim_score += abs(rlist[i] - llist[i])
#     return sim_score

# def part2(left_list, right_list):
#     sim_score = 0
#     for i in left_list:
#         sim_score += (i * right_list.count(i))
#     return sim_score


# print(part1(left_list, right_list))
# print(part2(left_list, right_list))