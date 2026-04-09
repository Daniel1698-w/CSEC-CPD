class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1],nums[i]=nums[i]*2, 0
        left=0
        right=1
        while left<len(nums) and right<len(nums):
            if nums[left]==0:
                right=left+1
                while right< len(nums) and nums[right]==0:
                    right+=1
                if right==len(nums):
                    break
                nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right+=1
        return nums
                

            