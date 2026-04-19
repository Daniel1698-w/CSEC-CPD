from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1=Counter(nums1)
        freq2= Counter(nums2)
        lis=[]
        for key , value in freq1.items():
            if key in freq2:
                lis.extend([key]*min(value, freq2[key]))
        return lis