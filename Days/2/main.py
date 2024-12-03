import copy
import dataclasses
from typing import List

@dataclasses.dataclass
class Report:
    levels: List[int]

    def is_consistent(self) -> bool:
        # check if all levels are either ascending or descending
        acs = self.levels.copy()
        dcs = self.levels.copy()

        acs.sort()
        dcs.sort(reverse=True)

        return self.levels == acs or self.levels == dcs

    def is_stepping(self) -> bool:
        # check if all neighbors are at least 1 apart and at most 3 apart
        return all(1 <= abs(self.levels[i] - self.levels[i+1]) <= 3 for i in range(len(self.levels) - 1))

    def is_valid(self) -> bool:
        return self.is_consistent() and self.is_stepping()

    def is_valid_supress(self, suppression_levels: int = 1) -> bool:
        if suppression_levels == 0:
            return self.is_valid()

        for i in range(len(self.levels)):
            new_levels = self.levels[:i] + self.levels[i + 1:]
            if Report(new_levels).is_valid_supress(suppression_levels - 1):
                return True
        return False


@dataclasses.dataclass
class Data:
    levels: List[Report]

    def count_valid(self, suppression_levels: int = 0) -> int:
        return sum(1 for r in self.levels if r.is_valid_supress(suppression_levels))


def load_input() -> Data:
    with open("input.txt") as f:
        return Data([Report([int(k) for k in r.split()]) for r in f.readlines()])

def main():
    data = load_input()

    print(f"Solution 1: {data.count_valid()}")
    print(f"Solution 2: {data.count_valid(1)}")

if __name__ == "__main__":
    main()
