
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

