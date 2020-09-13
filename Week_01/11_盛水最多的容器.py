class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针一定要想明白两个指针的实际含义，这里双指针代表所有可以作为容器边界的可能
        i, j = 0, len(height)-1
        nums = []
        vol = 0
        while i < j:
            if height[i] < height[j]:
                if vol < height[i]*(j-i):
                    vol = height[i]*(j-i)
                i += 1
            else:
                if vol < height[j]*(j-i):
                    vol = height[j]*(j-i)
                j -= 1
        return vol