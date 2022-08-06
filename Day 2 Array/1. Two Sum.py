class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
        ans=[]
        for j in range(len(nums)):
            if (target-nums[j]) in d and j!=d[target-nums[j]]:
                ans=[d[target-nums[j]],j]
                break
        return ans