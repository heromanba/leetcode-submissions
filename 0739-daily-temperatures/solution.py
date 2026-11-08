class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        mono_stack = []
        results = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            if not mono_stack:
                mono_stack.append((idx, temp))
                continue
            if temp <= mono_stack[-1][1]:
                mono_stack.append((idx, temp))
            else:
                while mono_stack and temp > mono_stack[-1][1]:
                    top_idx, top_temp = mono_stack.pop()
                    results[top_idx] = idx-top_idx
                mono_stack.append((idx, temp))
        while mono_stack:
            top_idx, top_temp = mono_stack.pop()
            results[top_idx] = 0
        return results



