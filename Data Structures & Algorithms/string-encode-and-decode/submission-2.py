class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a delimiter, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the next delimiter to extract the length
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            # Extract the actual string using the parsed length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next chunk
            i = j + 1 + length
            
        return res