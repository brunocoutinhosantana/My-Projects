
function upDate() {
    var select = document.getElementById('capacity');
    var value = select.options[select.selectedIndex].value; 
    
}
function growKg(e){
    var qtd = document.querySelector('input').value;
    var res = (e*0.001)*qtd;
    document.querySelector('.totKg').innerHTML = res;
}



