package laba1;
import org.junit.jupiter.api.Test;

import org.junit.jupiter.api.Assertions;


public class Problem2Test {

    @Test
    void test_1() {
        int[] a = {2, 1, 5, 6, 8};
        Problem2 problem2 = new Problem2();
        int[] actual = problem2.segregateEvenAndOddNumbers(a);
        int[] excepted = {2, 6, 8, 1, 5};
        Assertions.assertArrayEquals(excepted, actual);
    }
}