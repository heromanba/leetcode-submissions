class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        results = [0] * n
        for log in logs:
            func_id, act, time = log.split(':')
            func_id = int(func_id)
            time = int(time)
            if act == 'start':
                stack.append([func_id, act, time, 0])
            else:
                _, _, start_time, overlap = stack.pop()
                results[func_id] += (time-start_time-overlap+1)
                if stack:
                    stack[-1][-1] += (time-start_time+1)
        return results

