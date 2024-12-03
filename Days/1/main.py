from typing import List


def load_input() -> List[List[int]]:
    # expected list of pairs of integers
    with open("input.txt") as f:
        return [[int(k) for k in filter(lambda x: not not x, r.split())] for r in f.readlines()]

def parse_input(data: List[List[int]]) -> List[List[int]]:
    ret = [[] for _ in range(len(data[0]))]
    for v in data:
        for i, j in enumerate(v):
            ret[i] = [*ret[i], j]
    return ret

def main():
    data = load_input()
    data = parse_input(data)

    [v.sort() for v in data] # sort each list

    print(f"Solution 1: {sum([abs(i[0] - i[1]) for i in zip(*data)])}")

    count = {i: sum(1 for x in data[1] if x == i) for i in set(data[1])}

    print(f"Solution 2: {sum(j * count.get(j, 0) for j in data[0])}")

if __name__ == "__main__":
    main()