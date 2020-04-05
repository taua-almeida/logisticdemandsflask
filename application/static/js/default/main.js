const addpmbutton = document.getElementById("addpm");
const sendbutton = document.getElementById("sendpm");

document.getElementById("removepm").style.display = "none";

addpmbutton.addEventListener('click', function () {
    // Start of append
    let father = document.getElementById("pm");

    // Show remove button
    document.getElementById("removepm").style.display = "block";

    // All rows cloned
    let element = document.getElementById('pmrow');
    let cln = element.cloneNode(true);
    father.appendChild(cln);

}, false);

sendbutton.addEventListener("click", function (event) {
    event.preventDefault();
    let periods_values = [];
    let demands_values = [];

    let csrf_token = document.getElementById("csrf_token").value;

    let base = document.getElementById("base").value;
    let periods = document.getElementsByName('period');
    let demands = document.getElementsByName('demand');

    periods.forEach(element => periods_values.push(element.value));
    demands.forEach(element => demands_values.push(element.value));

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });

    $.ajax({
        url: "/default/calculatesma",
        method: 'POST',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({ "base" : base, "periods": periods_values, "demands": demands_values } ),
        success: function (data, result) {
            console.log(data);
        },
        error: function (error, textStatus, errorThrown) {
            console.log("Erro ao calcular");
        }
    })

}, false);

