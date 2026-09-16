class Solution:
    def minLights(self, lights: list[int]) -> int:
        illuminated = [False] * len(lights)
        light_interval = []
        for i in range(len(lights)):
            v = lights[i]
            if v > 0:
                start = max(0, i-v)
                end = min(len(lights)-1, i+v)
                light_interval.append((start, end))
        light_interval = sorted(light_interval)
        merged_interval = []
        curr_start, curr_end = None, None
        for i in range(len(light_interval)):
            if curr_start is None and curr_end is None:
                curr_start, curr_end = light_interval[i]
            if i+1 <= len(light_interval)-1:
                next_start, next_end = light_interval[i+1]
                if curr_end < next_start:
                    merged_interval.append((curr_start, curr_end))
                    curr_start, curr_end = None, None
                else:
                    if curr_end <= next_end:
                        curr_end = next_end
            if i == len(light_interval)-1:
                merged_interval.append((curr_start, curr_end))
        for start, end in merged_interval:
            for i in range(start, end+1):
                illuminated[i] = True
        additional = 0
        print(light_interval)
        for pos in range(len(illuminated)):
            if not illuminated[pos]:
                if pos + 1 < len(illuminated) and not illuminated[pos+1]:
                    illuminated[pos] = True
                    illuminated[pos+1] = True
                    if pos+2 < len(illuminated):
                        illuminated[pos+2] = True
                else:
                    illuminated[pos] = True
                additional += 1
        return additional
