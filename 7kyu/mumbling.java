// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

public class Accumul {
    public static String accum(String s) {
      String lowerS = s.toLowerCase();
      String[] strArr = lowerS.split("");
      String newS = "";
        for (int i=0; i<s.length(); i++) {
          String c = String.valueOf(lowerS.charAt(i));
          String upperC = c.toUpperCase();
          newS = newS + upperC;
          if (i > 0) {
            newS = newS + c.repeat(i);
          }
          if (i != s.length()-1) {
            newS = newS + "-";
          }
        }
      return newS;
    }
}