function clean() {
    res.innerHTML = ''
}
function insert(num){
    res.innerHTML += `${num}`
}
function back(){
    let res = document.getElementById('res').innerHTML;
    document.getElementById('res').innerHTML = res.substring(0, res.length -1);
}
function calcular(){
    let res = document.getElementById('res').innerHTML;
    if (res){
        document.getElementById('res').innerHTML = eval(res)
    }
}
