class Solution:
    def getLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            freq_map = {}
            freq_counter = {}
            for j in range(i, len(nums)):
                if nums[j] in freq_map:
                    old_freq = freq_map[nums[j]]
                    freq_counter[old_freq] -= 1 
                    if freq_counter[old_freq] == 0:
                        freq_counter.pop(old_freq)
                    freq_map[nums[j]] += 1
                else:
                    old_freq = 0
                    freq_map[nums[j]] = 1
                    
                new_freq = old_freq + 1
                if new_freq in freq_counter:
                    freq_counter[new_freq] += 1
                else:
                    freq_counter[new_freq] = 1

                if (len(freq_counter) == 1) and (len(freq_map)==1):
                    max_len = max(max_len, j-i+1)
                elif (len(freq_counter) == 2) and (max(freq_counter)/min(freq_counter) ==2):
                    max_len = max(max_len, j-i+1)
        return max_len


                    

