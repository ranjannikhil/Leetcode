class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                return len(s[i+1:])
            
            elif i==0:
                return len(s)
        
