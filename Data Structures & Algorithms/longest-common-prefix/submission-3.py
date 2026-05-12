class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorted_strs = sorted(strs)
        # for i in range(min(len(sorted_strs[0]), len(sorted_strs[-1]))):
        #     if sorted_strs[0][i] != sorted_strs[-1][i]:
        #         return sorted_strs[0][:i]
        # return sorted_strs[0]

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]