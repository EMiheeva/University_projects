package laba1;

import java.util.Arrays;
import java.util.Scanner;

public class Problem4 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Введите последовательность чисел через запятую, не используя пробел:");
        System.out.print("number = ");
        String user_sequence_of_number = in.nextLine();
        System.out.println(isGeometricProgression(user_sequence_of_number));
    }
    public static boolean isGeometricProgression(String numbers) {
        String[] number_from_user_sequence = numbers.split(",");
        final int size_array_b = number_from_user_sequence.length;
        double[] b = new double[size_array_b];

        //можно и int, т.к. в примере целые числа
        //но числа в прогрессии могут оказаться десятичными, поэтому я выбрала double
        //чтобы можно было представить как 7.0, так и 7
        for(int i = 0; i < number_from_user_sequence.length; i++){
            b[i] = Double.parseDouble(number_from_user_sequence[i]);
        }

        Arrays.sort(b);
        double q = b[1]/b[0];
        for(int n = 1; n < b.length-1; n++){
            if(b[n+1] == b[n] * q){
                return true;
            }
        }
        return false;
    }
}
