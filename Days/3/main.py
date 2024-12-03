import re

# This is such an abomination, xD
# I'm sorry for this, I just wanted to have fun with it

def solution1():
    with open("input.txt") as f:
        print(f"Solution 1:{sum(map(lambda x: int(x[0]) * int(x[1]), [(str(i).removeprefix("mul(").removesuffix(")").split(",")) for i in
                                                    re.findall(r"mul\(\d{1,3},\d{1,3}\)", f.read())]))}")


def solution2():
    with open("input.txt") as f:
        print(f"Solution 2:{sum(map(lambda x: int(x[0]) * int(x[1]), [(str(i).removeprefix("mul(").removesuffix(")").split(",")) for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(["".join(x.split("do()")[1::]) for x in [v if i != 0 else f"do(){v}" for i, v in enumerate(f.read().split("don't()"))]]))]))}")

if __name__ == "__main__":
    solution1()
    solution2()