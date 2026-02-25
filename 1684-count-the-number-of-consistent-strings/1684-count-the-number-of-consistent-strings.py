class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=len(words)
        allowed_Set=set(allowed)
        for word in words:
          
            for ch in word:
                
                if ch   not in allowed_Set:
                    count-=1
                    break
            
                
        return count             
                    
        