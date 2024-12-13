stones = {i:1 for i in open("./../inputs/test.txt", "r").readline().strip().split()}

stored_stones ={}

for ston in stones:
    print(ston)
print(stones)