// https://www.codewars.com/kata/57f780909f7e8e3183000078

public class Kata{
  public static int grow(int[] x){
    int total = 1;
    for (int num : x) {
      total *= num;
    }
    return total;
  }
}