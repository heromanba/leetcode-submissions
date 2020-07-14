class Solution {
private:
    int getNumDigits(int n) {
        int d = 0;
        while (n /= 10)
            d += 1;
        return d;
    }
public:
    int findNumbers(vector<int>& nums) {
        int num_even_digits = 0;
        for (int n : nums)
        {
            if (getNumDigits(n) % 2 != 0)
                num_even_digits += 1;
        }
        return num_even_digits;
    }
};
