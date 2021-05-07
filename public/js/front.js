const indexTrab = {
    arquivo: ""
}

const dadosLogin = {
    nomeUsuario: "",
    senha:""
}



//BOTAO EXTRAIR DADOS DO ARQUIVO CUJO NOME ESTÁ NO INDEXTRAB.ARQUIVO
function indexExtracaoDados() {

    indexTrab.arquivo = document.getElementById("bd").value;
    //alert(JSON.stringify(indexTrab));

}

//BOTAO DOWNLOAD DE PDF
function indexDownload() {

    indexTrab.arquivo = document.getElementById("bd").value;
    //alert(JSON.stringify(indexTrab));

}

function loginA(){

    dadosLogin.nomeUsuario = document.getElementById("nomeUsuarioA").value;
    dadosLogin.senha = document.getElementById("senhaA").value;

    //alert(JSON.stringify(dadosLogin));

}

function loginC(){

    dadosLogin.nomeUsuario = document.getElementById("nomeUsuarioC").value;
    dadosLogin.senha = document.getElementById("senhaC").value;

    //alert(JSON.stringify(dadosLogin));

}

//TEM QUE RECEBER PDF
const CadastroTrab = {

    titulo:"",
    autores:"",
    orientadores:"",
    instituicao:"",
    tipo:"",
    palavras:"",
    resumo:""
    //arquivo
}

//VALORES PRA SUBIR NO BD, INCLUINDO PDF
function enviarTrab() {

    CadastroTrab.titulo = document.getElementById("Titulo").value;
    CadastroTrab.autores = document.getElementById("Autores").value;
    CadastroTrab.orientadores = document.getElementById("Orientadores").value;
    CadastroTrab.tipo = document.querySelector('input[name="tipo"]:checked').value;
    CadastroTrab.resumo = document.getElementById("Resumo").value;

    alert(JSON.stringify(CadastroTrab));

}

const CadastroCord = {

    nome:"",
    data:"",
    email:"",
    telefone:"",
    departamento:"",
    observacoes:""

}

function enviarCord() {

    CadastroCord.nome = document.getElementById("nomeC").value;
    CadastroCord.data = document.getElementById("dateC").value;
    CadastroCord.email = document.getElementById("emailC").value;
    CadastroCord.telefone = document.getElementById("telefoneC").value;
    CadastroCord.departamento = document.getElementById("departamentoC").value;
    CadastroCord.observacoes = document.getElementById("resumoC").value;

    alert(JSON.stringify(CadastroCord));

}
