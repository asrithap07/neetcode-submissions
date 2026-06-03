class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            #compute signature
            signature = (0,) * 26
            for i in range(len(word)):
                letter = word[i]
                temp = list(signature)
                temp[ord(letter) - ord('a')]+=1
                signature = tuple(temp)
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]
        return list(groups.values())