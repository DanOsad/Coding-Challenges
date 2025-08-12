// https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

public class Solution {
  public static boolean validatePin(String pin) {
    for (int i=0; i<pin.length(); i++) {
      if (!Character.isDigit(pin.charAt(i))) {
        return false;
      }
    }
    switch (pin.length()) {
        case 4:
          return true;
        case 6:
          return true;
        default:
          return false;
    }
  }
}