def insertion_sort(collection):
    length = len(collection)
    for i in range(length):
        insert_idx = i
        while (
            insert_idx > 0 and 
            collection[insert_idx - 1][0] > collection[insert_idx][0]
        ):
            collection[insert_idx - 1], collection[insert_idx] = \
            collection[insert_idx], collection[insert_idx - 1]
            insert_idx -= 1
    return collection
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda x: x[0])

        merged_result = []

        for j in range(len(intervals_sorted)):
            # Initialize tmp var.
            if j == 0:
                merged_tmp = intervals_sorted[0]

            if j == len(intervals_sorted) - 1:
                merged_result.append(merged_tmp)
                break

            # Move the upper bound.
            if merged_tmp[1] >= intervals_sorted[j + 1][0]:
                lower = merged_tmp[0]
                upper = max(merged_tmp[1], intervals_sorted[j + 1][1])
                merged_tmp = [lower, upper]
            else:
                merged_result.append(merged_tmp)
                merged_tmp = intervals_sorted[j + 1]
        return merged_result
