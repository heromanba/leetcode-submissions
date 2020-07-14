class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_consecutive_size = 0;
        for (int i=0,j = 0; i < nums.size(); i = j)
        {            
            if (nums[i] != 1)
            {
                j++;
                continue;
            }
            
            for (j = i; j < nums.size(); j++)
            {
                if (nums[j] != 1)
                    break;
            }
            int size = j - i;
            if (size > max_consecutive_size)
                max_consecutive_size = size;
        }
        return max_consecutive_size;
    }
};
