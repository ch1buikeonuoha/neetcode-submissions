from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        EMPTY = []
        N = Counter(nums)
        pair = list(N.items())
        pair = sorted(pair, key=lambda x :x[1], reverse = True)
        pair = pair[0:k]
        return [item[0] for item in pair]