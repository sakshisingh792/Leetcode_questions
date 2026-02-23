class Solution:
   
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        res = 0
        min_val = -2**31
        max_val = 2**31 - 1
        n = len(s)

       
        while i < n and s[i] == " ":
            i += 1

       
        if i == n:
            return 0

        
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1

        
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

            if res * sign > max_val:
                return max_val
            if res * sign < min_val:
                return min_val

        return res * sign     




              



        