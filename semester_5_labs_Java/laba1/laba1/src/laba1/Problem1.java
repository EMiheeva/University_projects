package laba1;
import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("number = ");
        int user_number = in.nextInt();
        if (containsDigitAInHexadecimalRepresentation(user_number)){
            System.out.println(containsDigitAInHexadecimalRepresentation(user_number) + "( " + user_number + " = " + decimal_to_Hexadecimal_for_screen(user_number) + ", содержит А )");
        }
        else {
            System.out.println(containsDigitAInHexadecimalRepresentation(user_number) + "( " + user_number + " = " + decimal_to_Hexadecimal_for_screen(user_number) + ", не содержит А )");
        }
    }
    public static boolean containsDigitAInHexadecimalRepresentation(int number) {
        while (number > 0) {
            int mod_number = number % 16;
            number /= 16;
            if (mod_number == 10) {
                return true;
            }
        }
        return false;
    }
    public static String decimal_to_Hexadecimal_for_screen(int number) {
        StringBuilder hex_number = new StringBuilder();
        final String HEX_DIGITS = "0123456789ABCDEF";
        while (number > 0) {
            int new_number = number % 16;
            hex_number.insert(0, HEX_DIGITS.charAt(new_number));
            number /= 16;
        }
        return "0x" + hex_number;
    }
}