class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i,j in d.items():
            if j==1:
                return s.index(i)
        return -1