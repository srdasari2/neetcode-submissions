class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += "\\"
            for j in range(len(strs[i])):
                encodable = (ord(strs[i][j]) + 2) * 3
                encoded += "\\"
                encoded += str(encodable)
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = [""]
        print(s.split("\\"))
        spl = s.split("\\")
        if spl == ['']:
            return [] 
        counter =0
        for i in range(2, len(spl)):
            temp = spl[i]
            if not temp == '':
                tempint = int(temp)
                tempint = int(tempint / 3) - 2
                chartemp = chr(tempint)
                decoded[counter] += chartemp
            else:
                decoded.append("")
                counter += 1      
        return decoded