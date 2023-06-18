function entrar() {
    var email = document.getElementById("txte").value;
    var senha = document.getElementById("txts").value;

    if (email == "") {
        alert("Por favor, preencha o campo de e-mail.");
        return;
    }

    if (senha == "") {
        alert("Por favor, preencha o campo de senha.");
        return;
    }

    // Aqui você pode fazer uma chamada AJAX para verificar se o usuário está cadastrado no servidor
    // Por enquanto, vamos apenas verificar se o e-mail e a senha correspondem a um usuário válido
    if (email === "usuario@exemplo.com" && senha === "senha123") {
        // Usuário válido, realizar a ação de login
        console.log("Login bem-sucedido!");
    } else {
        // Usuário inválido, exibir mensagem de erro
        alert("Credenciais inválidas. Por favor, verifique seu e-mail e senha.");
    }
}