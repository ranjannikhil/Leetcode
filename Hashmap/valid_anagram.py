class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in map1:
                    map1.update({s[i]:map1[s[i]]+1})
                else:
                    map1[s[i]]=1

                if t[i] in map2:
                    map2.update({t[i]:map2[t[i]]+1})
                else:
                    map2[t[i]]=1
                


        if map1==map2:
            return True
        else:
            return False
        
