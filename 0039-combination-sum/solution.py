class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        results = []
        def backtrack(candidates, start, curr_list, curr_sum):
            if curr_sum == target:
                results.append(curr_list[:])
                return
            if curr_sum > target or start >= len(candidates):
                return
            curr_list.append(candidates[start])
            backtrack(candidates, start, curr_list, curr_sum+candidates[start])
            curr_list.pop()
            backtrack(candidates, start+1, curr_list, curr_sum)

        backtrack(candidates, 0, [], 0)
        return results
