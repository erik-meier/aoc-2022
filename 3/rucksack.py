import sys


def get_priority(c):
    return c - 96 if c > 90 else c - 38


def find_shared_items():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        mid = len(line) // 2
        first_half = set(line[:mid])
        second_half = set(line[mid:])
        value = ord(list(first_half.intersection(second_half))[0])
        total += get_priority(value)
    print(total)


def tally_items(index, items):
    for item in items:
        index[item] = index.get(item, 0) + 1
        if index[item] == 3:
            return get_priority(item)


def find_badges():
    total = 0
    for line in sys.stdin:
        set1 = set(line.strip())
        set2 = set(sys.stdin.readline().strip())
        set3 = set(sys.stdin.readline().strip())
        badge = list(set1.intersection(set2).intersection(set3))[0]
        total += get_priority(ord(badge))
    print(total)


if __name__ == '__main__':
    find_badges()
