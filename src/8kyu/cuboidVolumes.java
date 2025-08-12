// https://www.codewars.com/kata/58cb43f4256836ed95000f97

public class CuboidVolumes {
  public static int findDifference(final int[] firstCuboid, final int[] secondCuboid) {
    int firstVolume = 1;
    for (int i=0; i<firstCuboid.length; i++) {
      firstVolume *= firstCuboid[i];
    }
    int secondVolume = 1;
    for (int i=0; i<secondCuboid.length; i++) {
      secondVolume *= secondCuboid[i];
    }
    return (secondVolume - firstVolume > 0) ? secondVolume - firstVolume : firstVolume - secondVolume;
  }
}