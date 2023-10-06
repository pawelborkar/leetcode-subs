class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using hashmap

        dic = collections.defaultdict()

        #Iterate and sort the given words
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in dic:
                dic[sorted_word].append(word)
            else:
                dic[sorted_word] = [word]
        return dic.values()
        