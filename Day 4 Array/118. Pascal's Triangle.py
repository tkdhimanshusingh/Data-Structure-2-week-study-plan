class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            ans.append([0]*(i+1))
            for j in range(i+1):
                if j==0 or j==i:
                    ans[i][j]=1
                else:
                    ans[i][j]=ans[i-1][j]+ans[i-1][j-1]
        return(ans)