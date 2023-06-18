
// Array para armazenar os dados dos usuários
var usuarios = [];

// Função para cadastrar um novo usuário
function cadastrarUsuario() {
    // Obter os valores dos campos de entrada

    var nome = document.getElementById("txtnome").value;
    var email = document.getElementById("txte").value;
    var rua = document.getElementById("txtr").value;
    const numero = document.getElementById("txtnumero").value;
    var bairro = document.getElementById("txtb").value;
    var cidade = document.getElementById("txtc").value;
    var contato = document.getElementById("txtcont").value;
    var senha = document.getElementById("txts").value;

    // Criar um objeto para representar o novo usuário
    var novoUsuario = {
        nome: nome,
        email: email,
        rua: rua,
        numero: numero,
        bairro: bairro,
        cidade: cidade,
        contato: contato,
        senha: senha
    };

    // Adicionar o novo usuário ao array de usuários
    usuarios.push(novoUsuario);

    // Limpar os campos de entrada

    document.getElementById("txtnome").value = "";
    document.getElementById("txte").value = "";
    document.getElementById("txtr").value = "";
    document.getElementById("txtnumero").value = "";
    document.getElementById("txtb").value = "";
    document.getElementById("txtc").value = "";
    document.getElementById("txtcont").value = "";
    document.getElementById("txts").value = "";

    // Exibir uma mensagem de sucesso
    cadastrar();
    alert("Usuário cadastrado com sucesso!");
}

function validarNumeros(campo) {
    var numeros = /^[0-9]+$/;
    if (campo.value.match(numeros)) {
        return true;
    } else {
        alert('O campo ' + campo.name + ' deve conter somente números!');
        campo.focus();
        return false;
    }
}

function validarLetras(campo) {
    var letras = /^[A-Za-z\s]+$/;
    if (campo.value.match(letras)) {
        return true;
    } else {
        alert('O campo ' + campo.name + ' deve conter somente letras de A a Z ou de a a z!');
        campo.focus();
        return false;
    }
}
function validarEmail(campo) {
    var email = campo.value;
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        return true;
    } else {
        alert('Por favor, insira um endereço de e-mail válido!');
        campo.focus();
        return false;
    }
}

function validarCampos() {
    const nome = document.getElementById("txtnome");
    const email = document.getElementById("txte");
    const rua = document.getElementById("txtr");
    const bairro = document.getElementById("txtb");
    const cidade = document.getElementById("txtc");
    const contato = document.getElementById("txtcont");
    const senha = document.getElementById("txts");

    try {
        if (!validarLetras(nome)) throw new Error('txtnome');
        if (!validarEmail(email)) throw new Error('txte');
        if (!validarLetras(rua)) throw new Error('txtr');
        if (!validarLetras(bairro)) throw new Error('txtb');
        if (!validarLetras(cidade)) throw new Error('txtc');
    } catch (error) {
        alert('O campo ' + document.getElementById(error.message).name + ' deve ser preenchido corretamente!');
        document.getElementById(error.message).focus();
        return false;
    }

    return true;
}

function cadastrar() {
    if (!validarCampos()) {
        return;
    }

    // Obtém os valores dos campos do formulário
    const nome = document.getElementById("txtnome").value;
    const email = document.getElementById("txte").value;
    const rua = document.getElementById("txtr").value;
    const numero = document.getElementById("txtn").value;
    const bairro = document.getElementById("txtb").value;
    const cidade = document.getElementById("txtc").value;
    const contato = document.getElementById("txtcont").value;
    const senha = document.getElementById("txts").value;

    // Validação básica dos campos, verificando se estão preenchidos
    if (!nome || !email || !rua || !numero || !bairro || !cidade || !contato || !senha) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    // Aqui você pode adicionar código para enviar os dados do formulário para um servidor, 
    // realizar alguma ação no cliente, ou ambas as coisas. Um exemplo simples seria exibir
    // uma mensagem na tela para informar que o cadastro foi realizado com sucesso:
    alert("Cadastro realizado com sucesso!");
}