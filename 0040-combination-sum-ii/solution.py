class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        
        def backtrack(start, track, target):
            if target < 0:
                return
            
            if target == 0:
                res.append(track.copy())
                return
            
            if start == len(candidates):
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                backtrack(i+1, track, target - candidates[i])
                track.pop()
        
        backtrack(0, [], target)
        return res
            
