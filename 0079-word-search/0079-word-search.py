class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows = len(board) # length of row
        Cols = len(board[0]) # length of column
        path = set()
        
        def dfs(r, c, i):
            # r = current row |  c = current column | i is the index of word
            
            if i == len(word):
                return True #word found
            
            #out of bound cases 
            if r < 0 or c < 0 or r >=Rows or c >=Cols or word[i] !=board[r][c] or  (r,c) in path:
                return False
            
            path.add((r,c))
            
            # traverse 
            result = (dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1) or
                    dfs(r+1,c,i+1) or
                    dfs(r-1, c,i+1) )
                    
            path.remove((r,c))
            return result
        
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r,c,0) : return True
                
        return False
        
        
        