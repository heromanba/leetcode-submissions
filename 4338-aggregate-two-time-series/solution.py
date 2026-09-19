class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        merged_series = []
        i = 0
        j = 0
        while i < len(series1) and j < len(series2):
            s1_t, s1_v = series1[i]
            s2_t, s2_v = series2[j]
            if s1_t < s2_t:
                merged_series.append([s1_t, s1_v+s2_v])
                i += 1
            elif s1_t > s2_t:
                merged_series.append([s2_t, s1_v+s2_v])
                j += 1
            else:
                merged_series.append([s1_t, s1_v+s2_v])
                i += 1
                j += 1
        while i < len(series1):
            merged_series.append([series1[i][0], series1[i][1]])
            i += 1
        while j < len(series2):
            merged_series.append([series2[j][0], series2[j][1]])
            j += 1
        return merged_series

