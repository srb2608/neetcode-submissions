class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # s=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         a,b=nums[i] , nums[j]
        #         for k in range(len(nums)):
        #             if k==i or k==j:
        #                 continue
        #             elif a+b+nums[k]==0:
        #                 s.add(tuple([a,b,nums[k]]))
        # return s
        s=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[l] + nums[i] + nums[r]== 0:
                    s.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[l] + nums[i] + nums[r] <0:
                    l+=1
                else:
                    r-=1
        return s
