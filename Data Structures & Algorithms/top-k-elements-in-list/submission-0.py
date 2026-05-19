class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        uniques = {}

        for i, n in enumerate(nums):
            if n not in uniques:
                uniques[n] = 1
            else:
                uniques[n] += 1
        
        for l, v in uniques.items():
            bucket[v].append(l)

        result = []
        for i in reversed(bucket):
            for j in i:
                result.append(j)
                if len(result) == k:
                    return result