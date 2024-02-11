class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = self.frequency(ransomNote)
        mag = self.frequency(magazine)
        c=0
        for i in ransom:
            for j in mag:
                if i==j:
                    if mag[j]>=ransom[i]:
                        c=c+1
                
                        

        if c==len(ransom):
            return True
        else:
            return False
      
    def frequency(self,input_str:str)->dict:
      output_dict={}
      for i in input_str:
        if i in output_dict:
          c = output_dict[i]
          output_dict.update({i: c+1})
          
        else:
          output_dict[i] = 1

        
      return output_dict
        
