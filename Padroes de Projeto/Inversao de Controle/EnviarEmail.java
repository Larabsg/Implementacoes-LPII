public class EnviarEmail implements Enviar{

    public void execute(Usuario user) {
        System.out.println("Email enviado com sucesso!");
        System.out.println("Nome: " + user.nome());
        System.out.println("Email: " + user.email());
    }
    
}
