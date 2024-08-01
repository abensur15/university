// Importa a classe Scanner
import java.util.Scanner;

public class Fatorial {
    // Atributo da classe
    private int numero;

    // Método de acesso
    public int acessarNumero() {
        return this.numero;
    }

    // Método de modificação
    public void modificarNumero(int valor) {
        this.numero = valor;
    }

    // Função para calcular o fatorial recursivamente
    public int calcularFatorial(int num) {
        if(num == 1) {
            return num;
        }
        else {
            return num * calcularFatorial(num - 1);
        }
    }

    public static void main(String[] args) {
        // Criando o objeto Scanner
        Scanner teclado = new Scanner(System.in);

        // Criando o objeto da classe Fatorial
        Fatorial fat = new Fatorial();

        // Lendo o número
        int numero = teclado.nextInt();

        // Modificando o atributo número do objeto Fatorial
        fat.modificarNumero(numero);

        // Atribuindo à uma variavel o resultado do fatorial
        int resultado = fat.calcularFatorial(fat.acessarNumero());

        // Imprimindo o resultado
        System.out.println(resultado);
    }
}
