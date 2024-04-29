package laba1;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Problem2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Введите размер массива: ");
        final int user_size_array = in.nextInt();
        int[] user_array = new int[user_size_array];
        System.out.println("Введите элементы данного массива:");
        for (int i = 0; i< user_array.length; i++){
            user_array[i] = in.nextInt();
        }
        segregateEvenAndOddNumbers(user_array);
    }
    public static int[] segregateEvenAndOddNumbers(int[] array) {
        final int SIZE_ARRAY = array.length;
        int count_of_even_numbers = 0;
        int count_of_odd_numbers = 0;

        for (int i = 0; i < SIZE_ARRAY; i++){
            if (array[i] % 2 == 0){
                count_of_even_numbers += 1;
            }
            else {
                count_of_odd_numbers += 1;
            }
        }

        int[] array_of_even_numbers = new int[count_of_even_numbers];
        int[] array_of_odd_numbers = new int[count_of_odd_numbers];
        int index_even_numbers = 0;
        int index_odd_numbers = 0;
        for (int i = 0; i < SIZE_ARRAY; i++){
            if (array[i] % 2 == 0) {
                array_of_even_numbers[index_even_numbers] = array[i];
                index_even_numbers += 1;
            }
            else {
                array_of_odd_numbers[index_odd_numbers] = array[i];
                index_odd_numbers += 1;
            }
        }
        Arrays.sort(array_of_even_numbers);
        Arrays.sort(array_of_odd_numbers);
        System.out.println("Массив с чётными элементами: " + Arrays.toString(array_of_even_numbers));
        System.out.println("Массив с нечётными элементами: " + Arrays.toString(array_of_odd_numbers));

        int[] result_array = IntStream.concat(Arrays.stream(array_of_even_numbers), Arrays.stream(array_of_odd_numbers)).toArray();
        System.out.println("Результат конкатенации: " + Arrays.toString(result_array));
        return result_array;
    }


}
