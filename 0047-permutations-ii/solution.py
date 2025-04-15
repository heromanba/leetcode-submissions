class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.backtrack([], nums)
        return self.ret
        

    def backtrack(self, curr_list, remaining):
        if not remaining:
            if curr_list not in self.ret:
                self.ret.append(curr_list)
            return
        for i in range(len(remaining)):
            tmp_list = curr_list[:]
            tmp_list.append(remaining[i])
            self.backtrack(tmp_list, remaining[:i]+remaining[i+1:])
