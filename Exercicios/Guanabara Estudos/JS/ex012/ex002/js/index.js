var i = window.document.getElementById('idade')
var m = window.document.getElementById('masculino')
var f = window.document.getElementById('feminino')
var corpo = window.document.getElementById('corpo')
var dia = new Date()
var ano = dia.getFullYear()
var nasc = ano - i
function carregar() {
    if (i < 1940 || i > 2022) {
        window.alert('Você digitou um ano de nascimento invalido, por favor digite de novo')
    } else {
        resIdade.innerHTML = `Você tem ${nasc} anos`
    }
}