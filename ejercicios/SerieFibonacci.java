import java.util.Scanner;

public class SerieFibonacci {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el número de términos de la serie Fibonacci que desea generar:");
        int numTerminos = scanner.nextInt();

        System.out.println("La serie de Fibonacci hasta " + numTerminos + " términos es:");
        for (int i = 0; i < numTerminos; i++) {
            System.out.print(fibonacci(i) + " ");
        }
    }

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        int fib = 1;
        int prevFib = 1;
        for (int i = 2; i < n; i++) {
            int temp = fib;
            fib += prevFib;
            prevFib = temp;
        }
        return fib;
    }
}
