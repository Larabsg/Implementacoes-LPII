public class Main {

    public static void main(String[] args) {
        
        Usuario user = Usuario.criar(
            "Lara", 
            "88 1111-1111", 
            "lara@gmail.com"
            );

        new CadastrarUsuario().cadastro(user, new EnviarSMS());
        
    }
}