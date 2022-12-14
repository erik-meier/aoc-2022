import sys
import collections


def read_stacks():
    stacks = collections.defaultdict(list)
    for line in sys.stdin:
        if line[1] == '1':
            sys.stdin.readline()
            return stacks
        for stack_num in range(len(line)//4):
            symbol = line[(4*stack_num)+1]
            if symbol == ' ':
                continue
            stack = stacks[stack_num+1]
            stack.insert(0, symbol)


def transfer_one_at_a_time(stacks, amount, start, end):
    for _ in range(amount):
        stacks[end].append(stacks[start].pop())


def transfer_all_at_once(stacks, amount, start, end):
    stacks[end].extend(stacks[start][-amount:])
    stacks[start] = stacks[start][:len(stacks[start])-amount]


def rearrange(stacks):
    for line in sys.stdin:
        amount, line = line[4:].split(' from ')
        start, end = line.split(' to ')
        amount, start, end = map(int, [amount, start, end])
        transfer_all_at_once(stacks, amount, start, end)
    print(''.join(map(lambda i: stacks[i][-1], range(1, len(stacks)+1))))


if __name__ == '__main__':
    stacks = read_stacks()
    rearrange(stacks)
