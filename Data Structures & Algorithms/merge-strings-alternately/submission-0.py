class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        new_str = ""
        if l1 < l2:
            for i in range(l1):
                new_str = new_str + word1[i] + word2[i]
            new_str = new_str + word2[l1:]
        elif l2 < l1:
            for i in range(l2):
                new_str = new_str + word1[i] + word2[i]
            new_str = new_str + word1[l2:]
        else:
            for i in range(l1):
                new_str = new_str + word1[i] + word2[i]
        return new_str