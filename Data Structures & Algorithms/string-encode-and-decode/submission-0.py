class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += "#"
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delim_location = s.find('#', i)
            word_length = int(s[i:delim_location])
            start = delim_location + 1
            end = start + word_length
            word = s[start : end]
            decoded.append(word)
            i = end
        return decoded


