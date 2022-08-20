// https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1

public class CharProblem {
  public static int howOld(final String herOld) {
    String[] strSplit = herOld.split(" ");
    int age = Integer.parseInt(strSplit[0]);
    return age;
  }
}

// REFACTOR

public class CharProblem {
  public static int howOld(final String herOld) {
    return Integer.parseInt(herOld.split(" ")[0]);
  }
}