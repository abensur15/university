public class HelloWorld {
  public String texto;

  public String acessarTexto() {
    return this.texto;
  }

  public void modificarTexto(String texto) {
    this.texto = texto;
  }

  public void imprimirTexto() {
    System.out.println(this.acessarTexto());
  }

  public static void main(String[] args){
    HelloWorld helloWorld = new HelloWorld();
    helloWorld.modificarTexto("Hello, World!");
    helloWorld.imprimirTexto();
  }
}
