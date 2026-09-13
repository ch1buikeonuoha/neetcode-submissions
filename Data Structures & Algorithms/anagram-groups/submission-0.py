from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Y = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            Y[key].append(s)
        return list(Y.values())