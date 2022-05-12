function enviar() {
    let num = document.getElementById('txtn')
    let sel = document.getElementById('selnum')
     if (num.value.length == 0 || num.value == 0 || num.value > 100){
        window.alert('Numero invalido! Digite um numero entre 1 e 100')
    } else {
        let item = document.createElement('option')
        item.append(num)
        sel.appendChild(item)
    }
}