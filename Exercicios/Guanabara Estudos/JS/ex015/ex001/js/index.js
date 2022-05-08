function Calcular() {
    var inicio = window.document.getElementById('inicio')
    var final = window.document.getElementById('final')
    var passo = window.document.getElementById('passo')
    var res = window.document.getElementById('res')

    if(inicio.value.length == 0 || final.value.length == 0 || passo.value.length == 0){
        window.alert('Faltam Dados!')
        res.innerHTML = 'Impossivel contar!'
    } else {
        res.innerHTML = 'Contando: '
        let i = Number(inicio.value)
        let f = Number(final.value)
        let p = Number(passo.value)
        if (p <= 0){
            window.alert('Impossivel começar! Considerando passo 1')
            p = 1
        }
        if (i < f) {
            for (let index = i; index <= f; index += p) {
                res.innerHTML += `${index} 👉 `
            }
        }  else {
            for (let index = i; index <= f; index -= p) {
                res.innerHTML += `${index} 👉 `
            }
        }
    }
    res.innerHTML += `🏁`

}