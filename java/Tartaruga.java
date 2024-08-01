import java.util.Scanner;

public class Tartaruga{
    // Atributos da classe
    private float tamanho, crescimento;

    // Construtor da classe
    Tartaruga(float tam, float cresc){
        this.tamanho = tam;
        this.crescimento = cresc;
    }

    // Métodos de acesso
    public float acessarTamanho(){
        return this.tamanho;
    }

    public float acessarCrescimento(){
        return this.crescimento;
    }

    // Métodos de modificação
    public void modificarTamanho(float valor){
        this.tamanho = valor;
    }

    public void modificarCrescimento(float valor){
        this.crecimento = valor;
    }

    public void imprimirTempo(Tartaruga outra){
        // Tamanhos das tartarugas
        float tam1 = this.acessarTamanho();
        float tam2 = outra.acessarTamanho();
        
        // Crescimentos das tartarugas
        float cresc1 = this.acessarCrescimento();
        float cresc2 = outra.acessarCrescimento();

        // Cálculo do tempo
        float tempo = (tam2 - tam1) / (cresc2 - cresc1);

        // Imprime o resultado
        System.out.printf("%.2f", tempo);
    }

    public static void main(String[] args){
        // Cria o objeto da classe Scanner
        Scanner teclado = new Scanner(System.in);

        // Cria o objeto 1 da classe Tartaruga
        Tartaruga michelangelo = new Tartaruga(
            teclado.nextFloat(), teclado.nextFloat()
        );

        // Cria o objeto 2 da classe Tartaruga
        Tartaruga donatello = new Tartaruga(
            teclado.nextFloat(), teclado.nextFloat()
        );

        // Imprime o tempo
        michelangelo.imprimirTempo(donatello);
    }
}
