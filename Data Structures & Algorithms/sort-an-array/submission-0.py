class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums is None:
            return None
    
        l = len(nums)
        if l == 0 or l == 1:
            return nums
        else:
            list1 = nums[:l//2]
            list2 = nums[l//2:]

            return self.merge(self.sortArray(list1), self.sortArray(list2))
    
    def merge(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            l1 = len(list1)
            l2 = len(list2)

            if (l1 == 0 and l2 == 0):
                return []
            elif l1 == 0:
                return list2
            elif l2 == 0:
                return list1
            else:
                i = 0
                j = 0
                merged_list = []
                while i < l1 and j < l2:
                    if list1[i] <= list2[j]:
                        merged_list.append(list1[i])
                        i += 1
                    else:
                        merged_list.append(list2[j])
                        j+= 1
                if i < l1:
                    return merged_list + list1[i:]
                elif j < l2:
                    return merged_list + list2[j:]