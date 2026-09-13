from itertools import combinations
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        for (idx1, val1), (idx2, val2) in combinations(indexed_nums, 2):
            if val1 + val2 == target:
                return [idx1, idx2]
