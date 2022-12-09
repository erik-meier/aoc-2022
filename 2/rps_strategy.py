import sys


def evaluate_as_shape():
    values = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    results = {2: 0, 0: 3, 1: 6}
    score = 0
    for line in sys.stdin:
        shape1, shape2 = map(lambda s: values[s], line.split())
        score += results[(shape2 - shape1) % 3] + shape2
    print(score)

def evaluate_as_result():
    results = {'A X\n': 3,
               'A Y\n': 4,
               'A Z\n': 8,
               'B X\n': 1,
               'B Y\n': 5,
               'B Z\n': 9,
               'C X\n': 2,
               'C Y\n': 6,
               'C Z\n': 7}
    score = sum(map(lambda line: results[line], sys.stdin.readlines()))
    print(score)


if __name__ == '__main__':
    evaluate_as_result()
