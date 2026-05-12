class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        l1 = len(first)
        l2 = len(last)
        l = min(l1, l2)
        common = []
        for i in range(l):
            if first[i]==last[i]:
                common.append(first[i])
            else:
                return "".join(common)
        return "".join(common)