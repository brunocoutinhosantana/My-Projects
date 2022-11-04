
function insert(num) {
    var op = document.querySelector('.tela').innerHTML;
    document.querySelector('.tela').innerHTML = op + num;
}

function clean(){
    document.querySelector('.tela').innerHTML = '';
}

function calcular(){
    var resultado = document.querySelector('.tela').innerHTML;
    if(resultado) {
        document.querySelector('.tela').innerHTML = eval(resultado);
    } else {
        document.querySelector('.tela').innerHTML = 'Nada para calcular'
    }
}
