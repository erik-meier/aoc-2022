import sys


def count_contained():
    contained = 0
    for line in sys.stdin:
        assignment1, assignment2 = line.strip().split(',')
        start1, end1 = map(int, assignment1.split('-'))
        start2, end2 = map(int, assignment2.split('-'))
        if start1 > start2 and end1 > end2:
            continue
        elif start1 < start2 and end1 < end2:
            continue
        contained += 1
    print(contained)


def count_overlapped():
    overlapped = 0
    for line in sys.stdin:
        assignment1, assignment2 = line.strip().split(',')
        start1, end1 = map(int, assignment1.split('-'))
        start2, end2 = map(int, assignment2.split('-'))
        if end2 >= start1 >= start2:
            overlapped += 1
        elif end1 >= start2 >= start1:
            overlapped += 1
    print(overlapped)


if __name__ == '__main__':
    count_overlapped()
