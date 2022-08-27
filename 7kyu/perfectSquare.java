// https://www.codewars.com/kata/54c27a33fb7da0db0100040e

public class Square {    
    public static boolean isSquare(int n) { 
      double sqrt = Math.sqrt(n);
      if (sqrt == Math.floor(sqrt)) {
        return true;
      }
      return false;
  }
}