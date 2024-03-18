import java.math.BigDecimal;
import java.math.RoundingMode;

class Solution {
    public boolean isPerfectSquare(int num) {
        return (double)num==Math.pow(Math.round(Math.sqrt(num)),2);
    }
}
