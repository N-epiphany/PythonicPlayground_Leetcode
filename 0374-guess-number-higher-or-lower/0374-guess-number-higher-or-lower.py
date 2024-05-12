# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start =1
        end = n
        
        while start <= end :
            ans = start + (end - start) // 2
            
            if guess(ans) == 0:
                return ans
            
            elif (guess(ans) == -1):
                end = ans-1
                
            else:
                start = ans+1
                
        return None
                
           