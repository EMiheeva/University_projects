package laba1;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class Problem1Test {

    @Test
    void test_1() {
        int number = 10;
        Problem1 problem1 = new Problem1();
        boolean actual = Problem1.containsDigitAInHexadecimalRepresentation(number);
        assertTrue(actual);
    }

    @Test
    void test_2() {
        int number = 9;
        Problem1 problem1 = new Problem1();
        boolean actual = Problem1.containsDigitAInHexadecimalRepresentation(number);
        assertFalse(actual);
    }

}