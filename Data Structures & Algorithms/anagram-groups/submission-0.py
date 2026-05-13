class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = {}
        for i, w in enumerate(strs):
            w_sorted = "".join(sorted(w))
            if w_sorted in anag_dict:
                anag_dict[w_sorted].append(w)
            else:
                anag_dict[w_sorted] = [w]
        return list(anag_dict.values())