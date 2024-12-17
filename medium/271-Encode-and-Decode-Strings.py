"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and 
is decoded back to the original list of strings.
"""


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        l = r = 0

        while r < len(s):
            while s[r] != "#":
                r += 1

            length = int(s[l:r])
            output.append(s[r+1:r+1+length])

            l = r + 1 + length
            r = l
            
        return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
