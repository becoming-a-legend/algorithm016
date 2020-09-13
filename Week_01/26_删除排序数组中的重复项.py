class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针，与移动0差不多
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1