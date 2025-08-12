// https://www.codewars.com/kata/56269eb78ad2e4ced1000013

public class NumberFun {
    public static long findNextSquare(long sq) {
        if (Math.sqrt(sq) % 1 != 0) {
          return -1;
        }
        else {
          int nextN = (int)Math.floor(Math.sqrt(sq)) + 1;
          return (long)nextN * nextN;
        }
    }
  }