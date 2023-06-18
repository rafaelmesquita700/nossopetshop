function validarHorario(hora) {
    var horaMinima = 8; // hora mínima permitida
    var horaMaxima = 17; // hora máxima permitida
    var partesHora = hora.split(':'); // separa a hora em horas e minutos
    var horaAtual = parseInt(partesHora[0]); // obtém a hora atual

    if (horaAtual < horaMinima || horaAtual > horaMaxima) {
        return false;
    } else if (horaAtual == horaMinima && parseInt(partesHora[1]) == 0) {
        // se a hora for igual à hora mínima e os minutos forem 0, é permitido
        return true;
    } else if (horaAtual == horaMaxima && parseInt(partesHora[1]) == 0) {
        // se a hora for igual à hora máxima e os minutos forem 0, é permitido
        return true;
    } else {
        return true;
    }
}


function validarData(data) {
    var dataAtual = new Date();
    var dataInserida = new Date(data);

    if (dataInserida < dataAtual) {
        alert('A data inserida é anterior à data atual!');
        return false;
    }

    return true;
}

function validarLetras(campo) {
    var letras = /^[A-Za-z ]+$/;
    if (campo.value.match(letras)) {
        return true;
    } else {
        alert('O campo ' + campo.name + ' deve conter somente letras de A a Z ou de a a z!');
        campo.focus();
        return false;
    }
}

function validarCampos() {
    var nomeP = document.getElementById('txtnomepet');
    var tipoP = document.getElementById('txttp');
    var raca = document.getElementById('txtr');
    var resp = document.getElementById('txtresp');
    var dia = document.getElementById('txtd');
    var hora = document.getElementById('txth');

    try {

        if (!validarLetras(nomeP)) throw new Error('txtnomepet');
        if (!validarLetras(tipoP)) throw new Error('txttp');
        if (!validarLetras(raca)) throw new Error('txtr');
        if (!validarLetras(resp)) throw new Error('txtresp');

        if (!validarHorario(hora.value)) {
            erro = 'txth';
            alert('O campo ' + hora.name + ' deve estar entre as 8h e as 17h!');
            document.getElementById(erro).focus();
            return false;

        }
        if (hora.value == '') {
            erro = 'txth';
            alert('Preencha o horário!');
            document.getElementById(erro).focus();
            return false;
        }

        // Validar data
        if (!validarData(dia.value)) {
            erro = 'txtd';
            document.getElementById(erro).focus();
            return false;
        }

        if (dia.value <= 0 || hora.value < 0) {
            throw new Error('txtd');
        }
    } catch (error) {
        alert('O campo ' + document.getElementById(error.message).name + 'só aceita caracteres alfabéticos e deve ser preenchido corretamente!Por favor tente novamente!');
        document.getElementById(error.message).focus();
        return false;
    }

    return true;
}

function entrar() {
    if (!validarCampos()) {
        return;
    }

    var nomeP = document.getElementById('txtnomepet');
    var tipoP = document.getElementById('txttp');
    var raca = document.getElementById('txtr');
    var resp = document.getElementById('txtresp');
    var dia = document.getElementById('txtd');
    var hora = document.getElementById('txth');

    // validação dos campos
    if (nomeP.value == '' || tipoP.value == '' || resp.value == '' || dia.value <= 0 || hora.value < 0) {
        window.alert('Preencha todos os campos obrigatórios');
        return;
    }

    var fsex = document.getElementsByName('radsex');
    var np = nomeP.value;
    var tp = tipoP.value;
    var r = resp.value;
    var d = dia.value;
    var h = hora.value;
    var raca = raca.value;
    var tipo = '';

    if (fsex[0].checked) {
        tipo = 'O Banho e Tosa';
    } else if (fsex[1].checked) {
        tipo = 'A Consulta Médica';
    } else if (fsex[2].checked) {
        tipo = 'O Adestramento';
    }

    var mensagem = ` ${tipo} do(a) ${np} \n ${tp} \nRaça: ${raca} \nResponsável: ${r} \nFicou marcado para o dia: ${d} \nHorário: ${h} \nAgradecemos sua preferência! Até o dia do atendimento!`;
    alert(mensagem);
}