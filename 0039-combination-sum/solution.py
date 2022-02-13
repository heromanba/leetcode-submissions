class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        def backtrack(results, current_combination, candidates, target):
            current_sum = sum(current_combination)
            if current_sum > target:
                return
            if current_sum == target:
                results.add(tuple(sorted(current_combination)))
            for i, c in enumerate(candidates):
                backtrack(results, current_combination + [c], candidates[i:], target)
        backtrack(results, [], candidates, target)
        return results
