from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        set_p=Counter(p)
        length=len(p)
        ans=[]
        for i in range(len(s)+1):
            if i+length>len(s):
                return ans
            if s[i] in set_p:
                curr= Counter(s[i:i+length])
                if curr==set_p:
                    ans.append(i)
            i+=1

