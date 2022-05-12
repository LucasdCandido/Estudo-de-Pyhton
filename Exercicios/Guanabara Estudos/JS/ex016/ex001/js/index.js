function enviar() {
    let num = document.getElementById('txtn')
    let sel = document.getElementById('selnum')
     if (num.value.length == 0 || num.value == 0 || num.value > 100){
        window.alert('Numero invalido! Digite um numero entre 1 e 100')
    } else {
        let n = Number(num.value)
        let item = document.createElement('option')
        item.append(n)
        sel.appendChild(item)
    }
    
}
function checar(){
    let num = document.getElementById('txtn')
    let sel = document.getElementById('selnum')
    if (sel.option[sel.selectedAllIndex].Number == 0){
        window.alert('Digite algum numero primeiro!')
    } else {
        alert('click');
    }
    // alert("clicou");
}
