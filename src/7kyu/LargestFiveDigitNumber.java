// https://www.codewars.com/kata/51675d17e0c1bed195000001

public class LargestFiveDigitNumber {
    public static int solve(final String digits) {
      int val = 0;
        for (int i = 0; i < digits.length() - 4; i++) {
            int newVal = Integer.parseInt(digits.substring(i,i+5));
            val = newVal > val ? newVal : val;
        }
        return val;
    }
}