class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passengers_no_merge = []
        for num_i, from_i, to_i in trips:
            passengers_no_merge.append([from_i, num_i])
            passengers_no_merge.append([to_i, -num_i])
        passengers_no_merge = sorted(passengers_no_merge, key=lambda x: x[0])
        passengers = []
        for item in passengers_no_merge:
            if len(passengers) > 0 and item[0] == passengers[-1][0]:
                passengers[-1][1] += item[1]
            else:
                passengers.append(item)
        num_passengers = 0
        for item in passengers:
            num_passengers += item[1]
            if num_passengers > capacity:
                return False
        return True

