
// Validación suscripción 
function validarSuscripcion() {
  let suscripcion = document.getElementById("suscribirse");
  let formatoEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (suscripcion.value === "" || !formatoEmail.test(suscripcion.value)) {
    suscripcion.classList.add("is-invalid");
    suscripcion.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    suscripcion.classList.add("is-valid");
    suscripcion.classList.remove("is-invalid");
    alert("Gracias por suscribirte.");
    return true;
  }
}


// Validaciones Login
// Validación correo

function validarCorreo() {
  let correo = document.getElementById("email");
  let formatoEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (correo.value === "" || !formatoEmail.test(correo.value)) {
    correo.classList.add("is-invalid");
    correo.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    correo.classList.add("is-valid");
    correo.classList.remove("is-invalid");
    return true;
  }
}

// Validación contraseña
function validarContrasena() {
  let contrasena = document.getElementById("password");

  if (contrasena.value === "") {
    contrasena.classList.add("is-invalid");
    contrasena.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    contrasena.classList.add("is-valid");
    contrasena.classList.remove("is-invalid");
    return true;
  }
}

// Validación Login
function validarLogin() {
  if (validarCorreo() && validarContrasena()) {
    alert("Ingreso exitoso.");
    $('#modalPerfiles').modal('show'); // Va el ID del modal
    return true;
  } else {
    return false;
  }
}

// Validación modal Contacto
function validarCampos() {
    var nombre = document.getElementById("nombre_contacto");
    var asunto = document.getElementById("asunto_contacto");
    var mensaje = document.getElementById("mensaje_contacto");
    var correo = document.getElementById("correo_contacto");
    var correoVal = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    if (nombre.value === "" || asunto.value === "" || !correoVal.test(correo.value) || mensaje.value === "") {
      nombre.classList.add("is-invalid");
      nombre.classList.remove("is-valid");
      asunto.classList.remove("is-valid");
      asunto.classList.add("is-invalid");
      correo.classList.remove("is-valid");
      correo.classList.add("is-invalid");
      mensaje.classList.remove("is-valid");
      mensaje.classList.add("is-invalid");
      $('#modalError').modal('show'); // Modal Error
      $('#modalError').on('hidden.bs.modal', function (e) { // Para que al cerrar el modal de error, se abra nuevamente el de formulario
        $('#modalFormulario').modal('show'); // Modal formulario
      });
      return false;
    } else {
      nombre.classList.add("is-valid");
      nombre.classList.remove("is-invalid");
      asunto.classList.add("is-valid");
      asunto.classList.remove("is-invalid");
      correo.classList.add("is-valid");
      correo.classList.remove("is-invalid");
      mensaje.classList.add("is-valid");
      mensaje.classList.remove("is-invalid");
      $('#modalEnvio').modal('show'); // Modal envío
      return true;
    }
  }

  function validarCamposArt(){
    var nombreObra = document.getElementById("nameObra");
    var nombreArt = document.getElementById("nameArt");
    var tecnica = document.getElementById("tecnica");
    var precio = document.getElementById("precio");
    var estado = document.getElementById("estado");
    var imagen = document.getElementById("imagen");

    if (nombreObra.value === "" || nombreArt.value === "" || tecnica.value === "" || precio.value === "" || 
    estado.value === "" || imagen.value === "" ) {
      nombreObra.classList.add("is-invalid");
      nombreObra.classList.remove("is-valid");
      nombreArt.classList.add("is-invalid");
      nombreArt.classList.remove("is-valid");
      tecnica.classList.add("is-invalid");
      tecnica.classList.remove("is-valid");
      precio.classList.add("is-invalid");
      precio.classList.remove("is-valid");
      estado.classList.add("is-invalid");
      estado.classList.remove("is-valid");
      imagen.classList.add("is-invalid");
      imagen.classList.remove("is-valid");
      $('#modalError').modal('show'); // Modal Error
      $('#modalError').on('hidden.bs.modal', function (e) { // Para que al cerrar el modal de error, se abra nuevamente el de formulario
        $('#formModal').modal('show'); // Modal formulario
      });
      return false;
    } else {
      nombreObra.classList.add("is-valid");
      nombreObra.classList.remove("is-invalid");
      nombreArt.classList.add("is-valid");
      nombreArt.classList.remove("is-invalid");
      tecnica.classList.add("is-valid");
      tecnica.classList.remove("is-invalid");
      precio.classList.add("is-valid");
      precio.classList.remove("is-invalid");
      estado.classList.add("is-valid");
      estado.classList.remove("is-invalid");
      imagen.classList.add("is-valid");
      imagen.classList.remove("is-invalid");
      $('#modalEnvio').modal('show'); // Modal envío
      return true;
    }
  } 

function buscarArtista(){
      
  let arrArtista1 = ["Alfredo Smith", "AlfredoSmith.html" ];
  let arrArtista2 = ["Andres Cox", "AndresCox.html"];
  let arrArtista3 = ["Laura Hidalgo", "LauraHidalgo.html"];
  let arrArtista4 = ["Jose Roman", "JoseRoman.html"];
  let arrArtista5 = ["Camila Martinez", "CamilaMartinez.html"];
  let arrArtista6 = ["Pedro Machuca", "PedroMachuca.html" ];
  
  const arrArtistas = [arrArtista1, arrArtista2, arrArtista3, arrArtista4, arrArtista5, arrArtista6];
  
  artistaBuscar = document.getElementById("txtBuscarArtista").value;
      
  var mensaje="No se encuentra";
  for (let i=0; i < arrArtistas.length; i++) {
      // alert(arrArtistas[i]);
    if(arrArtistas[i].includes(artistaBuscar)){
        mensaje = "Se encontro!";
      if(confirm("Artista encontrado! Quieres visitar su galeria?")){
        link = arrArtistas[i][1];
        window.location.href = link;
      }
    }
  }
alert(mensaje);
}
  
  
//funcion para validar que la obra buscada se encuentre dentro de la pagina
/*funcion para validar la busqueda por obra, se crean varios array con las obras ordenadas por artista  y en el indice 0 se agrega el elemento link
estos array se ingresan a un array para posteriomente usar un for para la busqueda del elemento, una vez encontrado el elemento procede a preguntar si desea 
ser redirigido a la galeria donde esta la obra y con otro for se busca la posicion equivalente a el link y el usuario es llevado a la galeria donde se encuentra
la obra*/
function buscarObra(){
  
  let arrObrasAlfredoSmith = ["AlfredoSmith.html", "El entierro de kenny", "Vulva", "Stewie", "SpongeBob"];
  let arrObrasAndresCox = ["AndresCox.html", "Colour free", "Pubertad", "Interchange", "Iron Gogh", "La jeume fille a la perle", "Old glory", "Vincent Van Gogh night parodia mapa Google"];
  let arrObrasLauraHidalgo = ["LauraHidalgo.html", "Animales en la carcel", "Dia libre", "Primer beso", "Al acecho", "Chick lit", "Domingo peresozo", "Blues de dia lluvioso", "Mejoras para el hogar", "Retrato por encargo", "Yoga chick: pose de luciernaga", "Rata de gimnacio", "Su majestad", "Pastel del vaca", "Movimiento politico"];
  let arrObrasJoseRoman = ["JoseRoman.html", "Wild thing", "The wild things", "Whispering to myself", "Embraced #22", "Whispering to myself #1", "The wild thing #2", "Hallowed lady pinching and squeezing kettle"];
  let arrObrasCamilaMartinez = ["CamilaMartinez.html", "Abstratker bild", "Chaos, numero2", "Composicion VII", "numero 7: edad adulta"];
  let arrObrasPedroMachuca = ["PedroMachuca.html", "Big C", "Lola home", "Maison en vogue", "Peces en el agua"];

  const arrObras = [arrObrasAlfredoSmith, arrObrasAndresCox, arrObrasLauraHidalgo, arrObrasJoseRoman, arrObrasCamilaMartinez, arrObrasPedroMachuca];

  obraBuscar = document.getElementById("txtBuscarObra").value;
      
    
  var mensaje="No se encuentra";
  for (let i=0; i < arrObras.length; i++) {
    if(arrObras[i].includes(obraBuscar)){
      mensaje = "Se encontro!";
      if(confirm("Obra encontrada! Quieres visitar su galeria?")){
        link = arrObras[i][0];
        window.location.href = link;
      }
    }
  }
  alert(mensaje);
  
    
}

//VALIDACION PARA ENVIO (ACEPTACION O RECHAZO) DE SOLICITUD PENDIENTE
function validarSolicitPend(){
  var comentario = document.getElementById("comentarioTextarea");
  var estado = document.getElementById("selecOption");
  
  
  if (estado.value === "" || comentario.value === ""){
    
    estado.classList.add("is-invalid");
    estado.classList.remove("is-valid");
    comentario.classList.add("is-invalid");
    comentario.classList.remove("is-valid");
    $('#modalError').modal('show'); // Modal Error
    $('#modalError').on('hidden.bs.modal', function (e) { // Para que al cerrar el modal de error, se abra nuevamente el de formulario
      $('#formSolicPend').modal('show'); // Modal formulario
    });
    return false;
  } else {
    estado.classList.add("is-valid");
    estado.classList.remove("is-invalid");
    comentario.classList.add("is-valid");
    comentario.classList.remove("is-invalid");
    $('#modalEnvio').modal('show'); // Modal envío
    return true;
  }
  
}
