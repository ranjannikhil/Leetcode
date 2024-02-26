class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        output = strs[0]
        for i in range(len(output)):
            for s in strs[1:]:
                if len(s)==i or s[i]!=output[i]:
                    return output[:i]
            

        return output
        
