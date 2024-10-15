from collections import OrderedDict
from typing import List

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique_order = OrderedDict()
        self.count = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.unique_order:
            return next(iter(self.unique_order))  # Return the first key in the ordered dictionary
        return -1

    def add(self, value: int) -> None:
        if value in self.count:
            # Increment count and remove from OrderedDict if it's no longer unique
            self.count[value] += 1
            if value in self.unique_order:
                del self.unique_order[value]
        else:
            # New unique value: add to both count and OrderedDict
            self.count[value] = 1
            self.unique_order[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
