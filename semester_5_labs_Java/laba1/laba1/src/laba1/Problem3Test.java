package laba1;
import org.junit.jupiter.api.Test;

import org.junit.jupiter.api.Assertions;

public class Problem3Test {
    @Test
    void test_1() {
        int[][] a = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};
        Problem3 problem3 = new Problem3();
        int[] actual = problem3.flattenMatrix(a);
        int[] excepted = {1, 4, 7, 2, 5, 8, 3, 6, 9};
        Assertions.assertArrayEquals(excepted, actual);
    }
}
