class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:


        time=[]

        for d, s in zip(dist,speed):   
            time.append(d/s)
        time.sort()
        for i in range(len(time)):
            if time[i]<=i:
                return i
        return len(time)           




        