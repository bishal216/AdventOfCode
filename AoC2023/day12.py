# lines = open("./inputs/day12.txt", "r").readlines()
lines = open("./inputs/test.txt", "r").readlines()
lines = [line.strip() for line in lines]

def separate_configs(lines):
    configs = []
    for line in lines:
        a, b = line.split(' ')
        configs.append((list(filter(lambda chunk: chunk != '', a.split('.'))), (list(map(int, b.split(','))))))
    return configs

def get_configs(config):
    possible_configs = []
    conf1, conf2 = config

    print(conf1, conf2)
    print(possible_configs)
    print('=========================')
    return possible_configs
def part1(lines):
    configs = separate_configs(lines)
    config_count = 0
    for config in configs:
        config_count += len(get_configs(config))
    return config_count


print(part1(lines))
