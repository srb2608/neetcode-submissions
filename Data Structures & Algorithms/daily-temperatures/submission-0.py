class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        for i in range(len(temperatures)):
            b=False
            for j in range(i+1, len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    a.append(j-i)
                    b=True
                    break  
            if not b:
                a.append(0)     
            
        return a


        