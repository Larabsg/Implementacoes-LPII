public class Usuario {
    private String nome;
    private String telefone;
    private String email;

    private Usuario(String nome, String telefone, String email) {
        this.nome = nome;
        this.telefone = telefone;
        this.email = email;

        validate();
    }

    public static Usuario criar(String nome, String telefone, String email) {
        return new Usuario(nome, telefone, email);
    }

    public void update(String nome, String email, String telefone) {
        this.nome = nome;
        this.email = email;
        this.telefone = telefone;

        validate();
    }

    private void validate() {
        if (nome.isEmpty() || nome == null) {
            throw new IllegalArgumentException("Nome é obrigatório!");
        }

        if (email.isEmpty() || email == null) {
            throw new IllegalArgumentException("Email é obrigatório!");
        }

        if (telefone.isEmpty() || telefone == null) {
            throw new IllegalArgumentException("Telefone é obrigatório!");
        }
    }

    public String email() {
        return email;
    }

    public String nome() {
        return nome;
    }

    public String telefone() {
        return telefone;
    }
}
