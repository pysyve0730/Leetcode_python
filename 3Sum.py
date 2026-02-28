class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tmp = []
        for i in nums:
            j = i+1
            for j in nums:
                if nums[i]+nums[i+1]+nums[i+2]==0:
                    tmp.append(nums[i])
                    tmp.append(nums[i+1])
                    tmp.append(nums[i+2])
            return tmp
