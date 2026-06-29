class Solution:
    def sign (self, s:str) -> str:
        sign_arr = [0]*26
        res = ""
        for ch in s:
            sign_arr[ord(ch)-97] +=1
        for i in range(len(sign_arr)):
            if sign_arr[i] != 0:
                res = res + chr(i+97) + str(sign_arr[i])
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}
        for s in strs:
            s_sign = self.sign(s)
            if s_sign in anagrams:
                anagrams[s_sign].append(s)
            else:
                anagrams[s_sign] = [s]
        
        for key in anagrams:
            res.append(anagrams[key])
        
        return res