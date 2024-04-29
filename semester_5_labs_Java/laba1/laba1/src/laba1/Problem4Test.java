package laba1;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class Problem4Test {
    @Test
    void test_1() {
        String str = "1,2,4,8,16";
        Problem4 problem4 = new Problem4();
        boolean actual = problem4.isGeometricProgression(str);
        assertTrue(actual);
    }

    @Test
    void test_2() {
        String str = "16,2,8,1,4";
        Problem4 problem4 = new Problem4();
        boolean actual = problem4.isGeometricProgression(str);
        assertTrue(actual);
    }
    @Test
    void test_3() {
        String str = "2,3,5";
        Problem4 problem4 = new Problem4();
        boolean actual = problem4.isGeometricProgression(str);
        assertFalse(actual);
    }
}
