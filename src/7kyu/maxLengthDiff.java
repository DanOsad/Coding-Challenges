// https://www.codewars.com/kata/5663f5305102699bad000056

import java.lang.Math;

class MaxDiffLength {
    public static int mxdiflg(String[] a1, String[] a2) {
        if (a1.length == 0 || a2.length == 0) {
          return -1;
        }
        int lDiff = 0;
        for (int i=0; i<a1.length; i++) {
          for (int j=0; j<a2.length; j++) {
            int a = Math.abs(a2[j].length() - a1[i].length());
            if (a > lDiff) {
              lDiff = a;
            }
          }
        }
        return lDiff;
    }
}