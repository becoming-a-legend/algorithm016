class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        # 两数交换，不需要额外处理0
        #         nums[i] = nums[j]
        #         i += 1 
        # for k in range(i, len(nums)):
        #     nums[k] = 0

        return nums
        