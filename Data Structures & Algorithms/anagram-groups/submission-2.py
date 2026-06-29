class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        #make signature for the current string (itll be a tuple)
        for str in strs:
            signature = self.makeSignature(str)

            #if the signautre is existing in hashmap add the string to that hasmaps group
            if signature in groups:
                groups[signature].append(str)
            
            #else make a new group with the strings character
            else:
                groups[signature] = [str]
            
        #return all the hashmap values as an array
        return list(groups.values())

    def makeSignature(self, str: String):
        sig = (0, ) * 26
        for letter in str:
            temp = list(sig)
            temp[ord(letter) - ord('a')] += 1
            sig = tuple(temp)
        return sig