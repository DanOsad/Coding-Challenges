// https://www.codewars.com/kata/5648b12ce68d9daa6b000099

import java.util.ArrayList;

class Metro {
  public static int countPassengers(ArrayList<int[]> stops) {
    int passengers = 0;
    for (int i=0; i<stops.size(); i++) {
      passengers += stops.get(i)[0];
      passengers -= stops.get(i)[1];
    }
    return passengers;
  }
}