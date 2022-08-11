public class EnviarSMS implements Enviar{

    public void execute(Usuario user) {
        System.out.println("SMS enviado com sucesso!");
        System.out.println("Nome: " + user.nome());
        System.out.println("Telefone: " + user.telefone());
    }
    
}
