class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag=True
        magazine=list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                flag=False
                break
            else:
                magazine.remove(ransomNote[i])
        return flag