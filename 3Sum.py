class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tmp = []
        for i in nums:
            j = i+1
            k = i+2
            if k<len(nums):
                if nums[i]+nums[j]+nums[k]==0:
                    tmp[i].append(nums[i])
                    tmp[i].append(nums[j])
                    tmp[i].append(nums[k])
            return tmp
