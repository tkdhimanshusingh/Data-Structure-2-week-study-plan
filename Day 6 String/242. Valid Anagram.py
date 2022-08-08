class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = collections.defaultdict(int)
        for i in s: d[i] += 1
        for j in t: d[j] -= 1
        return all(k == 0 for k in d.values())