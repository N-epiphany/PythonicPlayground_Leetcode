class Solution:
    def fib(self, n: int) -> int:
        
        memo = { i:-1 for i in range( n + 1 ) }
        
        def dp( n ) :
            
            if n==0: return 0
            
            if n== 1: return 1
            
            if memo[ n ] != -1: 
                return memo[ n ]
        
            else:
                memo[n] = dp(n-1) +dp(n-2)
                return memo[n]
            
        
        return dp(n) 
