class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = dict()
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size in group_dict:
                group_dict[size].append(i)
            else:
                group_dict[size] = [i]
        ret = []
        for size, groups in group_dict.items():
            if size < len(groups):
                for j in range(len(groups)//size):
                    ret.append(groups[j:j+size])
            else:
                ret.append(groups)
        return ret
