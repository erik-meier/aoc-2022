import sys


def find_max_calories():
    max_calories = 0
    calories = 0
    for line in sys.stdin:
        if line == '\n':
            max_calories = max(max_calories, calories)
            calories = 0
        else:
            calories += int(line)
    print(max_calories)


def update_top_3(new, top):
    if new > top[0]:
        top[2] = top[1]
        top[1] = top[0]
        top[0] = new
    elif new > top[1]:
        top[2] = top[1]
        top[1] = new
    else:
        top[2] = max(top[2], new)


def find_top_3_calories():
    max_calories = [0, 0, 0]
    calories = 0
    for line in sys.stdin:
        if line == '\n':
            update_top_3(calories, max_calories)
            calories = 0
        else:
            calories += int(line)
    print(sum(max_calories))


if __name__ == '__main__':
    find_top_3_calories()
