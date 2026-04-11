from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        di= Counter(nums)
        count=0
        keys= list(di.keys())
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                if abs(keys[i]-keys[j])==k:
                    count +=  di[keys[i]]* di[keys[j]]
        return count