class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter=set()
        for ch in sentence:
            if "a"<=ch<="z":
                letter.add(ch)
        return len(letter)==26        


        