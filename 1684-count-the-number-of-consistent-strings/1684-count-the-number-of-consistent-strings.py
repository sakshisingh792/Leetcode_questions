class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=len(words)
        for ch in words:
          
            for ch2 in ch:
                
                if ch2   not in allowed:
                    count-=1
                    break
            
                
        return count             
                    
        