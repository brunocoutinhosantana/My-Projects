function openPopUp(e) {
    let key = e;
    document.querySelector('.title').innerHTML = informationsJson[key].name;
    document.querySelector('.descrition').innerHTML = informationsJson[key].description;
    document.querySelector('.button a').href = informationsJson[key].link;
    document.querySelector('.courseWindowArea').style.opacity = 0;
    document.querySelector('.courseWindowArea').style.display = 'flex';
    setTimeout(()=>{
        document.querySelector('.courseWindowArea').style.opacity = 1;
    }, 200);
};
function closePopUp() {
    document.querySelector('.courseWindowArea').style.opacity = 0;
    document.querySelector('.courseWindowArea').style.display = 'none';
    setTimeout(()=>{
        document.querySelector('.courseWindowArea').style.opacity = 0;
    }, 200);
};