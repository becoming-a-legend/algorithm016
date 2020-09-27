class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = 0
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
                count += 1
            else:
                dic[i] = 1
                count += 1
        for j in t:
            if j in dic and dic[j] > 0:
                dic[j] -= 1
                count -= 1
            
        return True if count == 0 else False