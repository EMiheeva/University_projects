package laba1;
import java.util.Arrays;
import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Введите количество строк матрицы ");
        final int n = in.nextInt();
        System.out.println("Введите количество столбцов матрицы ");
        final int m = in.nextInt();

        int[][] user_matrix = new int[n][m];

        for(int i = 0; i < n; i++){
            System.out.print((i+1) + " строка: ");
            for(int j = 0; j < m; j++){
                user_matrix[i][j] = in.nextInt();
            }
        }
        flattenMatrix(user_matrix);
    }
    public static int[] flattenMatrix(int[][] matrix) {
        int[][] transposed_matrix = new int[matrix[0].length][matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                transposed_matrix[j][i] = matrix[i][j];
            }
        }
        /*проверка примера
        String a = Arrays.toString(transposed_matrix[0]);
        String b = Arrays.toString(transposed_matrix[1]);
        String c = Arrays.toString(transposed_matrix[0]);
        for (int[] ints : transposed_matrix) {
            System.out.println("столбец: " + Arrays.toString(ints));
        }
         */
        int[] result_matrix = new int[transposed_matrix[0].length * transposed_matrix.length];
        int index_result_matrix = 0;
        for(int k = 0; k < transposed_matrix.length; k++){
            for(int l = 0; l < transposed_matrix[k].length; l++){
                result_matrix[index_result_matrix] = transposed_matrix[k][l];
                index_result_matrix++;
            }
        }
        System.out.println("Результат: " + Arrays.toString(result_matrix));
        return result_matrix;
    }
}
