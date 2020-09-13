from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列
        if k == 0:
            return None
        if k == 1:
            return nums
        deq = deque()
        deq.append(nums[0])
        output = []
        for i in range(1, k):
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
        output.append(deq[0])
        for i in range(k, len(nums)):
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
            if deq[0] == nums[i-k]:
                deq.popleft()
            output.append(deq[0])
        return output

