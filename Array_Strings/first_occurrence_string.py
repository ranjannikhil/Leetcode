class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:i+x]:
                return i
            
        return -1
        
