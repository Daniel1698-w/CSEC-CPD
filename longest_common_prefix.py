class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        minimum=float("INF")
        def check(lis,indx):
            start=lis[0][indx]
            for i in lis:
                if i[indx]!=start:
                    return False
            return True

        for i in strs:
            minimum=min(minimum, len(i))

        j=0
        ans=''
        while j <minimum and check(strs,j):
            ans+=strs[0][j]
            j+=1
        return ans


        