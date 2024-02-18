class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map={}
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i] not in map:
                    n=t[i]
                    if n in list(map.values()):
                        return False
                    map[s[i]]=t[i]
                    
                else:
                    n = map[s[i]]
                    if n!=t[i]:
                        return False
            

      
        return True
