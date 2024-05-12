class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = n
        row = 1
                      
        while total > 0:
            total = total - row
            row += 1
            
        if total == 0:
            return (row-1)
        
        return (row-2)

        