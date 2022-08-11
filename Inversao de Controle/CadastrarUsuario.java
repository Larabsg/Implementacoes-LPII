public class CadastrarUsuario {

    public void cadastro(Usuario user, Enviar enviar) {
        System.out.println("Cadastro realizado com sucesso!");
        enviar.execute(user);
    }
    
}
