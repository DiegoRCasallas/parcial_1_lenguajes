public class Recursiva {
    public static int sumatoriaRecursiva(int n) {
        if (n == 0) {
            return 0;
        } else {
            return n + sumatoriaRecursiva(n - 1);
        }
    }

    public static void main(String[] args) {
        int[] valores = {100, 500, 900};
        for (int valor : valores) {
            long inicio = System.nanoTime();
            int resultado = sumatoriaRecursiva(valor);
            long fin = System.nanoTime();
            //  a segundos 
            double tiempoSegundos = (fin - inicio) / 1_000_000_000.0;
            System.out.printf("Sumatoria hasta %d: %d (Tiempo: %.6f segundos)%n", valor, resultado, tiempoSegundos);
        }
    }
}