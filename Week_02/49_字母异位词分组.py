class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        output = []
        for i in range(len(strs)):
            temp = sorted(strs[i])
            temp = ''.join(temp)
            if temp in dic:
                j = dic[temp]-1
                # if j < len(output):
                output[j].append(strs[i])
            else:
                output.append([strs[i]])
                dic[temp] = len(dic) + 1
        return output


# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()



ans = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(ans)