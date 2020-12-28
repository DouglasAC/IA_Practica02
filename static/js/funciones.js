async function abrirArchivo() {
    var file = document.getElementById('archivo').files[0];

    if (file) {

        imagen = await getBase64(file)
    } else {
        alert('No se pudo abrir el archivo');
    }
}

var imagenes = []

function getBase64(file) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {

        imagenes.push([file.name, reader.result])
    };
    reader.onerror = function (error) {
        console.log('Error: ', error);
    };
}


function Calcular() {


    if (imagenes.length < 6) {
        mostrarImagenes()
    } else {
        mostrarTabla()
    }
}

function mostrarImagenes() {
    $.ajax({
        async: false,
        contentType: 'application/json;  charset=utf-8',
        type: "POST",
        url: "/cincoomenos",
        data: JSON.stringify({
            imagenes: imagenes

        }),
        success: function (data, textStatus, jqXHR) {
            console.log(data)
            valores = data.respuesta
            console.log(valores)

            codigo = "<table class=\"default\" >\n";
            codigo += "<tr>\n";
            for (let x = 0; x < valores.length; x++) {

                codigo += "<td>Imagen " + (x + 1) + "</td>\n";
            }

            codigo += "</tr>\n";
            codigo += "<tr>\n";
            for (let x = 0; x < valores.length; x++) {
                codigo += "<td>" + "<img src=\"" + imagenes[x][1] + "\"></td>\n";
            }
            codigo += "</tr>\n";
            codigo += "<tr>\n";
            for (let x = 0; x < valores.length; x++) {
                codigo += "<td>" + valores[x] + "</td>\n";
            }
            codigo += "</tr>\n";
            codigo += "</table>\n";
            console.log(codigo)
            document.getElementById('imagenes').innerHTML = codigo;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus)
        }

    });
}

function mostrarTabla() {
    $.ajax({
        async: false,
        contentType: 'application/json;  charset=utf-8',
        type: "POST",
        url: "/masdecinco",
        data: JSON.stringify({
            imagenes: imagenes

        }),
        success: function (data, textStatus, jqXHR) {
            console.log(data)
            valores = data.respuesta
            console.log(valores)

            codigo = "<table class=\"default\" >\n";
            codigo += "<tr>\n";
            codigo += "<td>Universidad</td>\n";
            codigo += "<td>Exactitud del Modelo</td>\n";
            codigo += "</tr>\n";

            porcentaje = []

            for(let x = 0; x < valores.length; x++)
            {
                let bueno = valores[x][0]
                let malo = valores[x][1]
                let total = bueno + malo
                if (total == 0){
                    porcentaje.push("No se probo")
                }else{
                    porcentaje.push(bueno/total * 100)
                }
            }

            codigo += "<tr>\n";
            codigo += "<td>Usac</td>\n";
            codigo += "<td>"+ porcentaje[0] + "</td>\n";
            codigo += "</tr>\n";

            codigo += "<tr>\n";
            codigo += "<td>Landivar</td>\n";
            codigo += "<td>"+ porcentaje[1] + "</td>\n";
            codigo += "</tr>\n";

            codigo += "<tr>\n";
            codigo += "<td>Mariano</td>\n";
            codigo += "<td>"+ porcentaje[2] + "</td>\n";
            codigo += "</tr>\n";
            codigo += "<tr>\n";
            codigo += "<td>Marroquin</td>\n";
            codigo += "<td>"+ porcentaje[3] + "</td>\n";
            codigo += "</tr>\n";

            codigo += "</table>\n";
            console.log(codigo)
            document.getElementById('tabla').innerHTML = codigo;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus)
        }

    });
}