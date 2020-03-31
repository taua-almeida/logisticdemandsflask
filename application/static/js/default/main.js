const addpmbutton = document.getElementById("addpm");

addpmbutton.addEventListener('click', function () {
    let father = document.getElementById("pm");
    let element = document.getElementById("period");
    let cln = element.cloneNode(true);
    father.appendChild(cln);
}, false);

