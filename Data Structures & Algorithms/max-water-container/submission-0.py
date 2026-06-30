class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l=0
        r=len(heights)-1
        while l<r:
            ans = min(heights[l],heights[r])*(r-l)
            m= max(ans, m)

            if (heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return m
        # for i in range(len(heights)):
        #     if heights[i]>=heights[len(heights)-i-1]:
        #         a = abs(heights[len(heights)-1-i]*(len(heights)-2*i))        
        #     else:    
        #         a = abs(heights[i]*(len(heights)-2*i))
        #     if a>m:
        #         m=a
        # return m

                
        